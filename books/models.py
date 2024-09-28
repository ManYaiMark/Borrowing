from django.db import models
from users.models import CustomUser

# Create your models here.
class Books(models.Model):
  photo = models.CharField(max_length=100,null=True,blank=True)
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  category = models.CharField(max_length=100)
  description = models.TextField(blank=True,null=True)
  about = models.TextField(blank=True,null=True)
  available = models.BooleanField(default=True)
  
  def __str__(self):
    return self.title

  
class Borrow(models.Model):
  user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
  book = models.ForeignKey(Books,on_delete=models.CASCADE)
  borrow_deta = models.DateTimeField(auto_now_add=True)
  return_deta = models.DateTimeField(blank=True,null=True)
  returned = models.BooleanField(default=False)

  def __str__(self) :
    return f"{self.user.username} borrow {self.book.title}"