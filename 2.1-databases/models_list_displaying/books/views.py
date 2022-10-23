from django.core.paginator import Paginator

from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {'books': books}
    return render(request, template, context)

def books_view_by_date(request, p_date):
    template = 'books/books_list_by_date.html'
    books = Book.objects.all().order_by('pub_date')
    dates_list = Book.objects.values('pub_date').distinct('pub_date').order_by('pub_date')    
    paginator = Paginator(dates_list, 1)
    filter_date = p_date
    has_found = False
    for p in paginator.page_range:        
        pg = paginator.get_page(p)
        if str(pg.object_list.values()[0].get('pub_date')) == p_date:
            page_number = pg.number
            has_found = True
            break
    if not has_found: 
        page_number = 1
        page_obj = paginator.get_page(page_number)
        filter_date =page_obj.object_list.values()[0].get('pub_date')

    b_by_date = books.filter(pub_date=filter_date)
    page_obj = paginator.get_page(page_number)

    if page_obj.has_previous():
        prev_page = paginator.get_page(page_obj.previous_page_number())
        prev_date = prev_page.object_list.values()[0].get('pub_date')
    else:
        prev_date = None

    if page_obj.has_next():
        next_page = paginator.get_page(page_obj.next_page_number())
        next_date = next_page.object_list.values()[0].get('pub_date')
    else:
        next_date = None
    
    context = {
        'books': b_by_date, 
        'page': page_obj, 
        'prev_date': prev_date,
        'next_date': next_date,   
    }

    return render(request, template, context)