from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import BookForm
from .models import Books
from django.urls import reverse

# Create your views here.
class BookListView(ListView):
    template_name = 'books/index.html'
    model = Books
    paginate_by = 10

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class BookCreateView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'books/add.html'

    def get_success_url(self):
        return reverse('index')

class BookDetailView(DetailView):
    model = Books
    template_name = 'books/detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class BookUpdateView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'books/edit.html'

    def get_success_url(self):
        return reverse('index')

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'books/delete.html'

    def get_success_url(self):
        return reverse('index')