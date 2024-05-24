from django.contrib import admin
from .models import usermsg, indexmodel, booking, doctordata, department, About

# Register your models here
admin.site.register(About)
admin.site.register(usermsg)
admin.site.register(indexmodel)
admin.site.register(booking)
admin.site.register(doctordata)
admin.site.register(department)
