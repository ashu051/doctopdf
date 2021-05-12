from django.contrib import admin
from .models import Document
# Register your models here.
@admin.register(Document)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','document','uploaded_at','description']