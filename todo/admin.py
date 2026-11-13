from django.contrib import admin
from .models import *

# Register your models here.

class TodolistAdmin(admin.ModelAdmin):
    list_display = ( 'id', "title" , 'description' , 'is_completed')
    list_editable = ('is_completed',)
    search_fields = ('title',)



admin.site.register(Todolist , TodolistAdmin)