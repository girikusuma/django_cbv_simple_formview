from django.urls import path
from .views import ( 
    BookListView, 
    BookCreateView, 
    BookDetailView, 
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('add/', BookCreateView.as_view(), name='add'),
    path('book/<slug:slug>/', BookDetailView.as_view(), name='detail'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='edit'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='delete'),
]