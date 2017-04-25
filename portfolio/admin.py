from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ['id','title','category','summary','created_date']
    list_display_links = ['id','title']


