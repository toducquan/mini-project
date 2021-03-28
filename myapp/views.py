from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Library


def library(request):
    listStore = Library.objects.all()
    return render(
        request = request,
        template_name = 'store.html',
        context={
            'stores': listStore
        }
    )
 

def book(request, library_id):
    productList = Book.objects.filter(store_id__id = library_id)
    store = get_object_or_404(Library, id = library_id)
    store_name = store.store_name
    return render(
        request = request,
        template_name = 'index.html',
        context={
            'products': productList,
            'name': store_name
        }
    )

def view_book(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    return render(
        request = request,
        template_name = 'book.html',
        context={
            'book': book
        }
    )

def del_book(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    id1 = book.store_id
    book.delete()
    return redirect('/myapp/library/'+str(id1))

def add_book(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        book_price = request.POST.get('book_price')
        book_actor = request.POST.get('book_actor')
        store_id = request.POST.get('store_id')
        Book.objects.create(
            book_name = book_name,
            book_price = book_price,
            book_actor = book_actor,
            store_id = int(store_id)
        )
        return redirect('/myapp/library/'+store_id)

    return render(
        request = request,
        template_name = 'add_book.html'
    )

# Create your views here.
