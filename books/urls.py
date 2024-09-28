from .views import *
from django.urls import path,include

urlpatterns = [
  path('',home_page,name='home'),
  path('<int:book_id>',borrow,name='borrow'),
]