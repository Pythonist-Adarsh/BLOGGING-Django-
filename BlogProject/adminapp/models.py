from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=20,primary_key=False)
    catdate=models.DateField(max_length=10)

class Enquiry(models.Model):
 name=models.CharField(max_length=20)
 email=models.EmailField(max_length=20)
 message=models.TextField(max_length=200)


class Blogs(models.Model):
    title=models.CharField(max_length=40)
    category=models.CharField(max_length=20)
    image=models.URLField()
    description=models.TextField(max_length=200)
    blogdate=models.DateField(max_length=10)