from django.contrib import admin

from .models import  Story, Content, User

# Register your models here.

admin.site.register(Story)
admin.site.register(Content)
admin.site.register(User)