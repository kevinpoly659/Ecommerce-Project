from django.contrib import admin
from django.contrib import admin
from .models import men,men_detail,women,women_detail,ad

# Register your models here.
admin.site.register(men)
admin.site.register(men_detail)
admin.site.register(women)
admin.site.register(women_detail)
admin.site.register(ad)