from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from Book.forms import DFModelForm
from Book.models import Book


def home(request):
    return render(request, 'base.html')


def list_1(request):
    search = request.GET.get('search', '')
    books = Book.objects.all()
    page = request.GET.get('page', 1)
    if search:
        books = books.filter(title__icontains=search)
    paginator= Paginator(books,2)
    books= paginator.get_page(page)
    return render(request, 'list.html', {'list': books,'search':search})


def list_create(request):
    if request.method == 'POST':
        form = DFModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Book.objects.create(title=data.get('title'), author=data.get('author'), price=data.get('price'))
            return redirect('list')
        return render(request, 'create.html', {'form': form})
    form = DFModelForm()
    return render(request, 'create.html', {'form': form})


def delete_list(request, pk):
    books = Book.objects.get(id=pk)
    books.delete()
    return redirect('list')


def list_update(request, pk):
    books = Book.objects.get(id=pk)
    form = DFModelForm(instance=books)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'update.html', {'form': form})
