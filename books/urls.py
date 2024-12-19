from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('book/<int:book_id>/', views.borrow, name='borrow'),
]