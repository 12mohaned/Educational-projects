# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Majors(models.Model):
    Major_name = models.CharField(max_length =200)
    Major_Info = models.TextField()
    Tutors_slug = models.CharField(max_length =200,default=1)
    Courses_slug = models.CharField(max_length=200,default=1)
    class Meta :
        verbose_name_plural = "Majors"
    def __str__(self):
        return self.Major_name

class Courses(models.Model):
    Course_Code = models.CharField(max_length = 100)
    Course_name = models.CharField(max_length =200)
    Course_content = models.TextField()
    Majorname  = models.ForeignKey(Majors,verbose_name = "Majors")
    class Meta :
        verbose_name_plural = "Courses"
    def __str__(self):
        return self.Course_name
class Tutor(models.Model):
    tutor_name  = models.CharField(max_length =200)
    tutor_age   = models.IntegerField()
    tutor_bio   = models.TextField()
    course_name  = models.ForeignKey(Courses,verbose_name = "Courses")
    class Meta :
        verbose_name_plural = "Tutors"
    def __str__(self):
        return self.tutor_name
    #def __str__(self):
    #    return "Number of Available Tutors for " + self.Major_name + " is " + str(self.number_of_Tutors)
class CoursesName(models.Model):
    course_name= models.ForeignKey(Courses,verbose_name = "Courses",on_delete=models.CASCADE,default = "")
    tutor_name = models.ForeignKey(Tutor,verbose_name = "Tutors",on_delete=models.CASCADE,default = "")
    Major_name = models.ForeignKey(Majors,verbose_name = "Majors",on_delete=models.CASCADE,default = "")
    def __str__(self):
        return self.course_name.Course_name
