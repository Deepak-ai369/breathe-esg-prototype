from django.contrib import admin
from .models import Tenant, EmissionRecord

admin.site.register(Tenant)
admin.site.register(EmissionRecord)
