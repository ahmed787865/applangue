from django import forms

from teachers.models import Teacher, Language
from users.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.shortcuts import redirect, render, get_object_or_404



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','phone_number', 'password')


class teacherForm(forms.ModelForm):
    language = forms.ModelChoiceField(queryset=Language.objects.all())

    class Meta:
        model = Teacher
        fields = ('name', 'phone_number', 'niveau_etude','experience','language')

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'phone_number')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class EditteacherForm(forms.ModelForm):
   # language = forms.ModelMultipleChoiceField(
    #    queryset=Language.objects.all(),
    #    widget=forms.Select,
    #    to_field_name='name',
    #    required=False)

    class Meta:
        model = Teacher
        fields = ('name', 'phone_number', 'niveau_etude','experience','language')

        def __init__(self, *args, **kwargs):
            super(EditteacherForm, self).__init__(*args, **kwargs)
            # Customize the language field widget (optional)
            self.fields['language'].widget.attrs = {'class': 'custom-language-dropdown'}

class langueForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('name',)

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
    }


class EditlangueForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('name',)

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
    }
