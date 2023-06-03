from django.shortcuts import render,redirect,reverse
from .models import Category,Enquiry,Blogs
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from blogapp.models import AdminLogin
import datetime
# Create your views here.

def adminhome(request):
    try:
        if request.session['adminid'] is not None:
            return render(request,"adminhome.html")
    except KeyError:
        render(request,"login.html")
def category_add(request):
   return  render(request,"category_add.html")
def category_show(request):
   try:
       if request.session['adminid'] is not None:
           cat=Category.objects.all()
           return render(request,'category_show.html',{'cat':cat})
   except KeyError:
    return  render(request,"category_show.html")
def enquiry(request):
    return render(request,"enquiry.html")
def create_category(request):
    category=request.POST['category']
    catdate=datetime.datetime.today()
    Cat=Category(category=category,catdate=catdate)
    Cat.save()
    return redirect('adminhome.html')
def delete_category(request,id):
 d=Category.objects.get(id=id)
 d.delete()
 return redirect('adminapp:adminhome')

def blog_add(request):
    try:
        if request.session['adminid'] is not None:
            cat = Category.objects.all()
            return render(request, 'blog_add.html', {'cat': cat})
    except KeyError:
     return render(request,"blog_add.html")
def blog_show(request):
     try:
         if request.session['adminid'] is not None:
            blog=Blogs.objects.all()
            return render(request,'blog_show.html',{'blog':blog})
     except KeyError:
        return render(request,'blog_show.html')
def deleteblog(request,id):
    d=Blogs.objects.get(id=id)
    d.delete()
    return redirect('adminapp:adminhome')

def create_enquiry(request):
    name=request.POST['uname']
    email=request.POST['email']
    message=request.POST['message']
    Enq=Enquiry(name=name,email=email,message=message)
    Enq.save()
    return redirect("adminhome.html")
def create_blog(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name, myfile)
        url =fs.url(filename)
        blog=Blogs(
            title=request.POST['title'],
            category=request.POST['category'],
            image=url,
            description=request.POST['description'],
            blogdate=datetime.datetime.today()

        )
        blog.save()
        return redirect('adminhome.html')
    else:
        pass

def  logout(request):
    try:
        if request.session['adminid'] is not None:
            """return  redirect(reverse('inherit'))"""
            return render(request,'login.html')
    except ObjectDoesNotExist:
        return render(request,'adminhome.html')
