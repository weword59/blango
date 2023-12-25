from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
import logging

logger = logging.getLogger(__name__)



# Create your views here.
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    
    logger.debug("Got %d posts", len(posts))

    return render(request, "blog/index.html", {"posts": posts})

def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    
    logger.info(
        "Created comment on Post %d for user %s", post.pk, request.user
    )
    return render(request, "blog/index.html", {"post": post})