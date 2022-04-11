from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect

from .models import Author, CategoryBook, Publisher, BookEn, BookItem
from .forms import AuthorForm, CategoryBookForm, PublisherForm, BookForm, BookItemForm

# Create your views here.
class Book(View):
    def get(self, request):
        bookItems = BookItem.objects.all()
        return render(request, 'book/book.html', {
            'bookItems': bookItems,
        })

class BookController(View):
    def get(self, request):
        authorList = Author.objects.all()
        categoryBooks = CategoryBook.objects.all()
        publishers = Publisher.objects.all()
        books = BookEn.objects.all()
        bookItems = BookItem.objects.all()
        return render(request, 'book/bookController.html', {
            'authorList': authorList,
            'categoryBooks': categoryBooks,
            'publishers': publishers,
            'books': books,
            'bookItems': bookItems,
        })


#----------------------- Author ------------------------------
class AuthorFormView(View):
    def get(self, request):
        af = AuthorForm()
        return render(request, 'book/authorForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            authorForm = AuthorForm(request.POST)
            if authorForm.is_valid():
                authorForm.save()
                return HttpResponse('Them thanh cong')


class AuthorFormUpdateView(View):
    def get(self, request, id):
        author = Author.objects.get(id=id)
        af = AuthorForm(instance=author)
        return render(request, 'book/authorForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            author = Author.objects.get(id=id)
            authorForm = AuthorForm(request.POST, instance=author)
            if authorForm.is_valid():
                authorForm.save()
                return redirect('/book/bookController')


class AuthorFormDeleteView(View):
    def get(self, request, id):
        author = Author.objects.get(id=id)
        af = AuthorForm(instance=author)
        return render(request, 'book/delete.html', {'af': af, 'item': author})
    def post(self, request, id):
        if request.method == 'POST':
            author = Author.objects.get(id=id)
            author.delete()
            return redirect('/book/bookController')

#----------------------- Category ------------------------------
class CategoryFormView(View):
    def get(self, request):
        af = CategoryBookForm()
        return render(request, 'book/authorForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            categoryForm = CategoryBookForm(request.POST)
            if categoryForm.is_valid():
                categoryForm.save()
                return redirect('/book/bookController')


class CategoryFormUpdateView(View):
    def get(self, request, id):
        category = CategoryBook.objects.get(id=id)
        af = CategoryBookForm(instance=category)
        return render(request, 'book/authorForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            category = CategoryBook.objects.get(id=id)
            categoryForm = CategoryBookForm(request.POST, instance=category)
            if categoryForm.is_valid():
                categoryForm.save()
                return redirect('/book/bookController')


class CategoryFormDeleteView(View):
    def get(self, request, id):
        category = CategoryBook.objects.get(id=id)
        af = AuthorForm(instance=category)
        return render(request, 'book/delete.html', {'af': af, 'item': category})
    def post(self, request, id):
        if request.method == 'POST':
            category = CategoryBook.objects.get(id=id)
            category.delete()
            return redirect('/book/bookController')


#----------------------- Publisher ------------------------------
class PublisherFormView(View):
    def get(self, request):
        af = PublisherForm()
        return render(request, 'book/authorForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            publisherForm = PublisherForm(request.POST)
            if publisherForm.is_valid():
                publisherForm.save()
                return redirect('/book/bookController')


class PublisherFormUpdateView(View):
    def get(self, request, id):
        publisher = Publisher.objects.get(id=id)
        af = PublisherForm(instance=publisher)
        return render(request, 'book/authorForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            publisher = Publisher.objects.get(id=id)
            publisherForm = PublisherForm(request.POST, instance=publisher)
            if publisherForm.is_valid():
                publisherForm.save()
                return redirect('/book/bookController')


class PublisherFormDeleteView(View):
    def get(self, request, id):
        publisher = Publisher.objects.get(id=id)
        af = PublisherForm(instance=publisher)
        return render(request, 'book/delete.html', {'af': af, 'item': publisher})
    def post(self, request, id):
        if request.method == 'POST':
            publisher = Publisher.objects.get(id=id)
            publisher.delete()
            return redirect('/book/bookController')


#----------------------- Book ------------------------------
class BookFormView(View):
    def get(self, request):
        af = BookForm()
        return render(request, 'book/authorForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            bookForm = BookForm(request.POST)
            if bookForm.is_valid():
                bookForm.save()
                return redirect('/book/bookController')
            else:
                HttpResponse('Các trường không họp lệ (có thể do trùng id)')
        else:
            HttpResponse('Các trường không họp lệ (có thể do trùng id)')


class BookFormUpdateView(View):
    def get(self, request, id):
        book = BookEn.objects.get(ISBN=id)
        af = BookForm(instance=book)
        return render(request, 'book/authorForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            book = BookEn.objects.get(ISBN=id)
            bookForm = BookForm(request.POST, instance=book)
            if bookForm.is_valid():
                bookForm.save()
                return redirect('/book/bookController')


class BookFormDeleteView(View):
    def get(self, request, id):
        book = BookEn.objects.get(ISBN=id)
        af = BookForm(instance=book)
        return render(request, 'book/delete.html', {'af': af, 'item': book})
    def post(self, request, id):
        if request.method == 'POST':
            book = BookEn.objects.get(ISBN=id)
            book.delete()
            return redirect('/book/bookController')

# ----------------------- BookItem ------------------------------
class BookItemFormView(View):
    def get(self, request):
        af = BookItemForm()
        return render(request, 'book/authorForm.html', {'af': af})

    def post(self, request):
        if request.method == 'POST':
            bookItemForm = BookItemForm(request.POST)
            if bookItemForm.is_valid():
                bookItemForm.save()
                return redirect('/book/bookController')
            else:
                HttpResponse('Các trường không họp lệ (có thể do trùng id)')
        else:
            HttpResponse('Các trường không họp lệ (có thể do trùng id)')

class BookItemFormUpdateView(View):
    def get(self, request, id):
        bookItem = BookItem.objects.get(barcode=id)
        af = BookItemForm(instance=bookItem)
        return render(request, 'book/authorForm.html', {'af': af})

    def post(self, request, id):
        if request.method == 'POST':
            bookItem = BookItem.objects.get(barcode=id)
            bookItemForm = BookItemForm(request.POST, instance=bookItem)
            if bookItemForm.is_valid():
                bookItemForm.save()
                return redirect('/book/bookController')

class BookItemFormDeleteView(View):
    def get(self, request, id):
        bookItem = BookItem.objects.get(barcode=id)
        af = BookItemForm(instance=bookItem)
        return render(request, 'book/delete.html', {'af': af, 'item': bookItem})

    def post(self, request, id):
        if request.method == 'POST':
            bookItem = BookItem.objects.get(barcode=id)
            bookItem.delete()
            return redirect('/book/bookController')