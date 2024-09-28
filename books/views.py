from django.http import HttpResponse
from django.shortcuts import render
from .models import Books
from .models import CustomUser

# Create your views here.
def home_page(request):
  all_books = Books.objects.order_by('title')
  context = { 'books' : all_books}
  return render(request,'books/home_page.html',context)

def borrow(request,book_id): 
  book = Books.objects.get(id=book_id)
  context = { 'book' : book }
  return render(request,'books/borrow.html',context)