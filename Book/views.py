from re import search
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Book.forms import DFModelForm
from Book.models import Book
from accounts.util import login_required


def home(request):
    return render(request, 'base.html')


class BookListView( LoginRequiredMixin,ListView,):
    model = Book
    template_name = 'list.html'
    context_object_name = 'list'
    paginate_by = 6

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        book = Book.objects.all()

        if search:
            book = Book.objects.filter(title__icontains=search)
        return book

    def get_context_data(self, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['search'] = \
            self.request.GET.get('search', '')
        return context


class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'create.html'
    form_class = DFModelForm
    permission_required = 'book.add_book'
    success_url = reverse_lazy('list')


class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'update.html'
    form_class = DFModelForm
    permission_required = 'book.change_book'
    success_url = reverse_lazy('list')
    pk_url_kwarg = 'pk'


class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('list')
    permission_required = 'book.delete_book'
    pk_url_kwarg = 'pk'
    template_name ='book_confirm_delete.html'


# def list_1(request):
#     search = request.GET.get('search', '')
#     books = Book.objects.all()
#     page = request.GET.get('page', 1)
#     if search:
#         books = books.filter(title__icontains=search)
#     paginator=Paginator(books,2)
#     books= paginator.get_page(page)
#     return render(request, 'list.html', {'list': books,'search':search})

# def list_create(request):
#     if request.method == 'POST':
#         form = DFModelForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Book.objects.create(title=data.get('title'), author=data.get('author'), price=data.get('price'))
#             return redirect('list')
#         return render(request, 'create.html', {'form': form})
#     form = DFModelForm()
#     return render(request, 'create.html', {'form': form})

#
# @login_required
# def delete_list(request, pk):
#     books = Book.objects.get(id=pk)
#     books.delete()
#     return redirect('list')
#
#
# @login_required
# @permission_required('book.delete_book', raise_exception=True)
# def list_update(request, pk):
#     books = Book.objects.get(id=pk)
#     form = DFModelForm(instance=books)
#     if form.is_valid():
#         form.save()
#         return redirect('list')
#     return render(request, 'update.html', {'form': form})
