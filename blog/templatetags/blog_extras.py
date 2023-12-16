from django.contrib.auth import get_user_model
from django import template

register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(author):
    if not isinstance(author, user_model):
       # return empty string as safe default
      return ""
      
    if author.first_name and author.last_name:
       name = f"{author.first_name} {author.last_name}"
    else:
       name = f"{author.username}"
    
    return nam

@register.simple_tag
def row():
    return '<div class="row">'


@register.simple_tag
def endrow():
    return "</div>" 

@register.simple_tag(takes_context=True)
def author_details_tag(context):
    request = context["request"]
    current_user = request.user
    post = context["post"]
    author = post.author

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html("{}{}{}", prefix, name, suffix)