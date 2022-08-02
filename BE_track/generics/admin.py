from django.contrib import admin

# Register your models here.
from .models import Generics

# Register your models here.
@admin.register(Generics)

class GenericModelAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'part', 'age', 'bio')
    list_editable = ('bio',)
    list_filter = ('part',)
    search_fields = ('id', 'name', 'part')