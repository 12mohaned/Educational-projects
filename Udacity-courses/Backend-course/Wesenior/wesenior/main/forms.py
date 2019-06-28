from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    Major=forms.CharField(label = 'Major name',required = True)
    age  = forms.IntegerField(label = 'Age',required = True)
    Bio  = forms.CharField(label = "Tell us more about you",required = True)

    class Meta :
        model = User
        fields = ("username","password1","password2","Major","age","Bio")

    def save(self,commit = True):
        user = super(TutorForm,self).save(commit = False)
        user.Major = self.cleaned_data['Major']
        user.age = self.cleaned_data['age']
        user.Bio = self.cleaned_data['Bio']

        if commit :
            user.save()
        return user
