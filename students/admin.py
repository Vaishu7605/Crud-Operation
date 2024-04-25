from django.contrib import admin
from .models import *
@admin.register(register)

class studentAdmin(admin.ModelAdmin):
    list_display=('id','name','age','phone','mail')



# Register your models here.
