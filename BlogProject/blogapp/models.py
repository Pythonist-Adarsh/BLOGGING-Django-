from django.db import models


# Create your models here.
class AdminLogin(models.Model):
    adminid = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)

class Contact(models.Model):
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    email=models.EmailField(max_length=20)
    message=models.TextField(max_length=200)


class BlogComment(models.Model):
    Blogid=models.IntegerField(max_length=50)
    comment=models.CharField(max_length=15)
    commentDate=models.DateField(max_length=20)