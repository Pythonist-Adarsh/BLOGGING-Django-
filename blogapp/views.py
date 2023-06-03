from django.shortcuts import render,redirect,reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import AdminLogin,Contact,BlogComment
from adminapp.models import Blogs,Category
import datetime
# Create your views here.
def index(request):
    try:
        if request.session['adminid'] is not None:
            blg=Blogs.objects.all()
            return render(request,'index.html',{'blg':blg})
    except KeyError:
      return render(request,'index.html')
def inherit(request):
    return render(request,'inherit.html')
def Contact_us(request):
    return render(request,'Contact_us.html')
def about(request):
    return render(request,'aboutus.html')
def password(request):
    return render(request,'password.html')
def blogs(request):
   try:
       if request.session['adminid'] is not None:
           cate=Category.objects.all()
           bl=Blogs.objects.all()
           return render(request,'blogs.html',{'cate':cate,'bl':bl})
   except KeyError:
       return render(request,'blogs.html')
def login(request):
    return  render(request,'login.html')
def validateuser(request):
    adminid=request.POST['email']
    password=request.POST['password']
    try:
       object=AdminLogin.objects.get(adminid=adminid,password=password)
       if object is not None:
           request.session['adminid']=adminid
           return redirect(reverse('adminapp:adminhome'))
    except ObjectDoesNotExist:
        return render(request,'login.html')

def contact(request):
    firstname=request.POST['fname']
    lastname=request.POST['lname']
    email=request.POST['email']
    message=request.POST['msg']
    con=Contact(firstname=firstname,lastname=lastname,email=email,message=message)
    con.save()
    return redirect('index.html')
