from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    all_books = [
        {
            'id': 1,
            'photo': 'https://m.media-amazon.com/images/I/71sH3vxziLL._AC_UF1000,1000_QL80_.jpg',
            'title': 'Harry Potter',
            'author': 'JK Rowling',
            'category': 'Fantasy',
            'description': 'This book is magical and loved by many.'
        },
        {
            'id': 2,
            'photo': 'https://m.media-amazon.com/images/I/81xrIOcHWVL._UF1000,1000_QL80_.jpg',
            'title': 'The Money Game',
            'author': 'George Goodman',
            'category': 'Non-fiction',
            'description': 'The Money Game explores the emotions and myths in financial markets.'
        },
        {
            'id': 3,
            'photo': 'https://m.media-amazon.com/images/M/MV5BMTA1NDQ3NTcyOTNeQTJeQWpwZ15BbWU3MDA0MzA4MzE@._V1_.jpg',
            'title': 'Pride and Prejudice',
            'author': 'Jane Austen',
            'category': 'Novel',
            'description': 'A novel of manners by Jane Austen, first published in 1813.'
        },
        {
            'id': 4,
            'photo': 'https://birlinn.co.uk/wp-content/uploads/2020/10/9781846975769.jpg',
            'title': '1984',
            'author': 'George Orwell',
            'category': 'Dystopian Fiction',
            'description': 'A cautionary tale by George Orwell, published in 1949.'
        }
    ]
    return render(request, 'books/home.html', {'books': all_books})


def borrow(request, book_id):
    all_books = [
        {
            'id': 1,
            'photo': 'https://m.media-amazon.com/images/I/71sH3vxziLL._AC_UF1000,1000_QL80_.jpg',
            'title': 'Harry Potter',
            'author': 'JK Rowling',
            'category': 'Fantasy',
            'description': 'This book is magical and loved by many.'
        },
        {
            'id': 2,
            'photo': 'https://m.media-amazon.com/images/I/81xrIOcHWVL._UF1000,1000_QL80_.jpg',
            'title': 'The Money Game',
            'author': 'George Goodman',
            'category': 'Non-fiction',
            'description': 'The Money Game explores the emotions and myths in financial markets.'
        },
        {
            'id': 3,
            'photo': 'https://m.media-amazon.com/images/M/MV5BMTA1NDQ3NTcyOTNeQTJeQWpwZ15BbWU3MDA0MzA4MzE@._V1_.jpg',
            'title': 'Pride and Prejudice',
            'author': 'Jane Austen',
            'category': 'Novel',
            'description': 'A novel of manners by Jane Austen, first published in 1813.'
        },
        {
            'id': 4,
            'photo': 'https://birlinn.co.uk/wp-content/uploads/2020/10/9781846975769.jpg',
            'title': '1984',
            'author': 'George Orwell',
            'category': 'Dystopian Fiction',
            'description': 'A cautionary tale by George Orwell, published in 1949.'
        }
    ]
    book = next((book for book in all_books if book['id'] == book_id), None)
    if not book:
        return HttpResponse("Book not found!", status=404)
    return render(request, 'books/book.html', {'book': book})