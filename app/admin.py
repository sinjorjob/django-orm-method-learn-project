from django.contrib import admin

from .models import School, Student

class SchoolAdmin(admin.ModelAdmin):
    list_display=('pk','name', 'email', 'address')

class StudentAdmin(admin.ModelAdmin):
    list_display=('pk','name', 'grade', 'school', 'blood_group', 'mobile', 'address')


admin.site.register(Student, StudentAdmin)
admin.site.register(School, SchoolAdmin)
