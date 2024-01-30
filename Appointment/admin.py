from django.contrib import admin

from .models import Doctor, Patient, Appointments, Departments, Visits, Login

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointments)
admin.site.register(Departments)
admin.site.register(Visits)
admin.site.register(Login)
