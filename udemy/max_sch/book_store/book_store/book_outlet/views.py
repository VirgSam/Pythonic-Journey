from django.shortcuts import render, get_object_or_404
from . models import Book
from django.http import Http404
from django.db.models import Avg, Min, Max
# Create your views here.

def index(request):
    books= Book.objects.all().order_by("title")
    num_books=books.count()
    avg_books=books.aggregate(Avg("rating"))
    min_books=books.aggregate(Min("rating"))
    max_books=books.aggregate(Max("rating"))

    return render(request,"book_outlet/index.html",
                  {
                      "books":books,
                      "total_number_of_books":num_books,
                      "average_rating":avg_books,
                      "min_rating":min_books,
                      "max_rating":max_books,
                   }
                  )

def book_detail(request, slug):
    # try:
    #     book= Book.objects.get(pk=id)
    # except:
    #     raise Http404
    book = get_object_or_404(Book, slug=slug) # this does the same job as lines 11-14
    return render(request,"book_outlet/book_detail.html",
                  {
                      "title":book.title,
                      "author":book.author,
                      "rating":book.rating,
                      "is_bestseller":book.is_bestselling,
                   })
