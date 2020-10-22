# # C:\Users\12482\Desktop\py_learn\Django2.0_chapter46\mysite_env\mysite\blog\admin.py
from django.contrib import admin
from .models import BlogType, Blog # , ReadNum

# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	# list_display = ('title', 'blog_type', 'author', 'get_read_num', 'created_time', 'last_updated_time')
	list_display = ('id', 'title', 'blog_type', 'author', 'get_read_num' ,'created_time', 'last_updated_time')

'''
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
	list_display = ('read_num', 'blog')
'''