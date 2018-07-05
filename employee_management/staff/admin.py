from django.contrib import admin
from staff.models import Employee, Department

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)