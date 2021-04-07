"""Django Views."""
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from main.forms import PostForm
from main.models import Post


def index(request):
    """Route main page."""
    return render(request, "main/index.html")


def about(request):
    """Route About."""
    return render(request, "main/about.html", {"title": "About Company"})


def posts(request):
    """Route Posts."""
    _posts = Post.objects.all()
    return render(request, "main/posts.html", {'title': "Posts", "posts": _posts})


def post_create(request):
    """Route Create Post."""
    errors = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            errors = "Cannot save the post"
    else:
        form = PostForm()
    context = {
        "form": form,
        "errors": errors
    }
    return render(request, "main/post_create.html", context=context)


def api_posts(request):
    """Route Posts API."""
    _posts = Post.objects.all()
    response_data = [dict(title=post.title, description=post.description, content=post.content) for post in _posts]
    return JsonResponse(response_data, safe=False)
