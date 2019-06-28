# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tutor ,Majors, Courses
# Register your models here.
class TutorAdmin(admin.ModelAdmin):
    fields = ["tutor_name","tutor_age","tutor_bio"]
admin.site.register(Tutor,TutorAdmin)
class MajorAdmin(admin.ModelAdmin):
    fields = ["Major_name","Major_Info","Tutors_slug","Courses_slug"]
admin.site.register(Majors,MajorAdmin)
class CoursesAdmin(admin.ModelAdmin):
    fields = ["Course_name","Course_content","Reserve_slug","Recommend_slug"]
admin.site.register(Courses,CoursesAdmin)
