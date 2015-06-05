from django.contrib import admin
from .models import User, PageItem

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'account',)
@admin.register(PageItem)
class PageItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes',)
