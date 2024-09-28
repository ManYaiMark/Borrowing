from django.db import models
from users.models import CustomUser
from books.models import Books
import requests
# Create your models here.

# class Borrow(models.Model):
#   user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#   book = models.ForeignKey(Books,on_delete=models.CASCADE)
#   borrow_deta = models.DateTimeField(auto_now_add=True)
#   return_deta = models.DateTimeField(blank=True,null=True)
#   returned = models.BooleanField(default=False)

#   def __str__(self) :
#     return f"{self.user.username} borrow {self.book.title}"

  
