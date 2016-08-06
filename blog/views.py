from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	## posts = Post.objects.filter(publicado_fecha__lte=timezone.now()).order_by('publicado_fecha')
	posts = Post.objects.all()

	return render(request, 'blog/post_list.html', {'posts': posts})