from django.contrib import admin

# Register your models here.

from.models import *

admin.site.register(Coffee)
admin.site.register(OrginPlace)
admin.site.register(MainProcessing)
admin.site.register(Grinding)