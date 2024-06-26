from django import forms

from teachers.models import Teacher, Language
from users.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.shortcuts import redirect, render, get_object_or_404


class UserForm(forms.ModelForm):
    username = forms.CharField(label="Phone Number",
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number', 'password')


class teacherForm(forms.ModelForm):
    language = forms.ModelChoiceField(queryset=Language.objects.all())

    class Meta:
        model = Teacher
        fields = ('name', 'phone_number', 'language')


class EditteacherForm(forms.ModelForm):
    language = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.Select,
        to_field_name='name',
        initial=Language.objects.all(),
        required=False)

    class Meta:
        model = Teacher
        fields = ('name', 'phone_number', 'language')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'niveau_etude': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),

        }


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
        fields = ('name', )

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
    }
