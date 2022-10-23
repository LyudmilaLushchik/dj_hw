from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {'books': books}
    return render(request, template, context)

def books_view_by_date(request, p_date):
    template = 'books/books_list_by_date.html'
    books = Book.objects.all()
    b_by_date = books.filter(pub_date=p_date)
    b_list = list(books)

    if b_list.index(b_by_date[0]) != 0:
        previous_date = Book.objects.get(id=b_list[b_list.index(b_by_date[0]) - 1].id).pub_date
    else:
        previous_date = None

    if b_list.index(b_by_date[0]) < len(books) - 1:
        next_date = Book.objects.get(id=b_list[b_list.index(b_by_date[0]) + 1].id).pub_date
    else:
        next_date = None

    context = {'books': b_by_date, 'previous_date': previous_date, 'next_date': next_date}

    return render(request, template, context)