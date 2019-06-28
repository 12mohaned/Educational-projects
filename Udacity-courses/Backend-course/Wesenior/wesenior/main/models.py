# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Majors(models.Model):
    Major_name = models.CharField(max_length =200)
    Major_Info = models.TextField()
    Tutors_slug = models.CharField(max_length =200)
    #Courses_slug = models.CharField(max_length=200)

class Courses(models.Model):
    Course_name = models.CharField(max_length =200)
    Course_content = models.TextField()
    #Reserve_slug= models.CharField(max_length =200)
    #Recommend_slug = models.CharField(max_length =200)
    #Majorname  = models.ForeignKey(Majors)

class Tutor(models.Model):
    tutor_name  = models.CharField(max_length =200)
    tutor_age   = models.IntegerField()
    tutor_bio   = models.TextField()
    course_name  = models.ForeignKey(Courses)

    def __str__(self):
        return "Tutor-name :" + self.tutor_name + "\n" + "tutor-age:" + str(self.tutor_age)+ "\n" + "tutor-bio :" + self.tutor_bio + "\n" + "Major" + Major

    #def __str__(self):
    #    return "Number of Available Tutors for " + self.Major_name + " is " + str(self.number_of_Tutors)
