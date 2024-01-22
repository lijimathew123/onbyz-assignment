from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'subject', 'passing_out_date', 'student_image')
    search_fields = ('name', 'student_class', 'subject')
    list_filter = ('passing_out_date',)

admin.site.register(Student,StudentAdmin)