from django.contrib import admin
from . models import catagories, brands, sub_catagories
# Register your models here.
admin.site.register(catagories)
admin.site.register(brands)
admin.site.register(sub_catagories)
