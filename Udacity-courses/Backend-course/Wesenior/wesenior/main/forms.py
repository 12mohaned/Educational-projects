from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tutor,Courses,Majors
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta :
        model = User
        fields = ("username","email","password1","password2")
    def save (self,commit = True):
        user = super(NewUserForm,self).save(commit = False)
        user.email =self.cleaned_data['email']
        if commit :
            user.save()
        return user
class TutorForm(UserCreationForm):

    Major=forms.CharField(label = 'Major name(MGT,MET,Pharmacy and Bio Technology,Applied Arts)',required = True)
    age  = forms.IntegerField(label = 'Age',required = True)
    Bio  = forms.CharField(label = "Tell us more about you",required = True)
    class Meta :
        model = User
        fields = ("username","password1","password2","email","Major","age","Bio")
    def save(self,commit = True):
        user = super(TutorForm,self).save(commit = False)
        user.Major = self.cleaned_data['Major']
        user.age = self.cleaned_data['age']
        user.Bio = self.cleaned_data['Bio']
        #T = Tutor(tutor_name = user.username,tutor_age = user.age,tutor_bio = user.Bio,course_name = Courses(None).save() )
        #T.save()
        if commit :
            user.save()
        return user
Tutors = [tuple([i.tutor_name.capitalize(),i.tutor_name]) for i in Tutor.objects.all()]
class ChooseTutor(forms.Form):
    field = forms.ChoiceField(widget = forms.Select,choices = Tutors)
