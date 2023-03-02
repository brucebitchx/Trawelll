from django.contrib import admin
from .models import Packages, Places, Travel

admin.site.register(Packages)
admin.site.register(Places)
admin.site.register(Travel)