from django import forms

from teachers.models import Teacher





class ImageForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name ','phone','language')