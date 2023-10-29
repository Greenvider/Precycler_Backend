from django.contrib import admin
from .models import Member, Stores, Inquiry

# Register your models here.
admin.site.register(Member)
admin.site.register(Stores)
admin.site.register(Inquiry)