from django.contrib import admin
from .models import Sponsor, Student, University, SponsorShip
# Register your models here.

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'money', 'status']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'university', 'degree', 'contract']

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(SponsorShip)
class SponsorShipAdmin(admin.ModelAdmin):
    list_display = ['id', 'sponsor', 'student', 'money']