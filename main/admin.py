from django.contrib import admin
from .models import Locomotive, Run, Branch, Year


admin.site.register(Branch)
admin.site.register(Locomotive)
admin.site.register(Run)
admin.site.register(Year)
