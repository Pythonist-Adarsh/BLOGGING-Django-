from django.contrib import admin
from . models import AdminLogin,Contact,BlogComment
# Register your models here.
admin.site.register(AdminLogin)
admin.site.register(Contact)
admin.site.register(BlogComment)