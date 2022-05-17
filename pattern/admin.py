from django.contrib import admin
from .models import ClassPattern, SHACLPattern

# Register your models here.
admin.site.register(ClassPattern)
admin.site.register(SHACLPattern)
