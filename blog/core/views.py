from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, Tag

# Create your views here.

def index(request):
    
    return redirect('blog')


def blog(request):

    blog = Post.objects.order_by("created_at")

    tags = Tag.objects.order_by("id")


    return render(request, "blog.html", {
        'list':blog,
        'tags':tags})


def tag(request):

    tags = Tag.objects
    teste = "teste_tag"

    return render(request, "blog.html", {
        'list_tags':tags,
        'testetag':teste})