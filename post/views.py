from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from Book.forms import DFModelForm
from accounts.util import login_required
from post.forms import SDModelForm
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})


@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=id)
    return render(request, 'posts/detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = SDModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(title=data.get('title'), author=data.get('author'))
            return redirect('post/list')
        return render(request, 'posts/create.html', {'form': form})
    form = SDModelForm()
    return render(request, 'posts/create.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user == post.author:
        post.delete()
        return redirect('post/list')
    else:
        return redirect('post/list')


@login_required
def add_comment(request, pk):
    post = Post.objects.get(pk=pk)
