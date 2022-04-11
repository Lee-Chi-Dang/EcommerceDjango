from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.Book.as_view(), name='book'),
    path('bookController/', views.BookController.as_view(), name='bookController'),
    path('authorForm/', views.AuthorFormView.as_view(), name='authorForm'),
    path('updateAuthorForm/<int:id>', views.AuthorFormUpdateView.as_view(), name='authorFormUpdate'),
    path('deleteAuthorForm/<int:id>', views.AuthorFormDeleteView.as_view(), name='authorFormDelete'),
    path('categoryForm/', views.CategoryFormView.as_view(), name='categoryForm'),
    path('updateCategoryForm/<int:id>', views.CategoryFormUpdateView.as_view(), name='categoryFormUpdate'),
    path('deleteCategoryForm/<int:id>', views.CategoryFormDeleteView.as_view(), name='categoryFormDelete'),
    path('publisherForm/', views.PublisherFormView.as_view(), name='publisherForm'),
    path('updatePublisherForm/<int:id>', views.PublisherFormUpdateView.as_view(), name='publisherFormUpdate'),
    path('deletePublisherForm/<int:id>', views.PublisherFormDeleteView.as_view(), name='publisherFormDelete'),
    path('bookForm/', views.BookFormView.as_view(), name='bookForm'),
    path('updateBookForm/<int:id>', views.BookFormUpdateView.as_view(), name='bookFormUpdate'),
    path('deleteBookForm/<int:id>', views.BookFormDeleteView.as_view(), name='bookFormDelete'),
    path('bookItemForm/', views.BookItemFormView.as_view(), name='bookItemForm'),
    path('updateBookItemForm/<int:id>', views.BookItemFormUpdateView.as_view(), name='bookItemFormUpdate'),
    path('deleteBookItemForm/<int:id>', views.BookItemFormDeleteView.as_view(), name='bookItemFormDelete'),
]
