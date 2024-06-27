from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import teacherForm, EditteacherForm, UserForm, langueForm, EditlangueForm, EditUserForm
from .models import Teacher, Language
from users.models import User
from django.views.generic import (CreateView, DeleteView, ListView, UpdateView)
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

@login_required
def home(request):

    return render(request, 'home.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


class LoginView(LoginView):
    template_name = 'login.html'  # Adjust as needed

    def get_success_url(self):
        # Redirect to dashboard after successful login
        return reverse('home')  # Assuming you have a 'dashboard:home' URL pattern

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to dashboard if already logged in
        return super().dispatch(request, *args, **kwargs)


class Allteachers(ListView):
    model = Teacher
    context_object_name = "teachers"
    template_name = "teachers.html"
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get("q")
        queryset = Teacher.objects.all()
        if q != None:
            queryset = queryset.filter(Q(username__icontains=q) | Q(phone_number__icontains=q))
        return queryset


def createTeacher(request):
    if request.method == 'POST':
        form = teacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            #  client.user_type = "C"
            #  client.set_password(request.POST.get('password'))
            teacher.save()
            return redirect('Enseignants')  # Redirect to a view displaying the list of clients
    else:
        form = teacherForm()

    return render(request, 'new_teacher.html', {'form': form})


class Editteacher(UpdateView):
    model = Teacher
    template_name = 'update_teacher.html'
    form_class = EditteacherForm
    success_url = reverse_lazy('Enseignants')

    def form_valid(self, form):
        pk = self.kwargs['pk']
        teacher = get_object_or_404(Teacher, pk=pk)
        form.save()
        messages.success(self.request, 'Client  edited successfully.')
        return super().form_valid(form)


def DeleteTeacher(request, pk):
    model = Teacher
    teacher = Teacher.objects.filter(id=pk)
    teacher.delete()
    # template_name = 'delete_user.html'
    messages.success(request, 'teacher  deleted successfully.')
    return redirect('Enseignants')


def teacher_details(request, pk):
    order = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teacher_details.html', locals())


class langues(ListView):
    model = Teacher
    context_object_name = "langues"
    template_name = "langues.html"
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get("q")
        queryset = Language.objects.all()
        if q != None:
            queryset = queryset.filter(Q(username__icontains=q) | Q(phone_number__icontains=q))
        return queryset


def DeleteLangue(request, pk):
    model = Language
    langue = Language.objects.filter(id=pk)
    langue.delete()
    # template_name = 'delete_user.html'
    messages.success(request, 'langue  deleted successfully.')
    return redirect('langues')


def createLangue(request):
    if request.method == 'POST':
        form = langueForm(request.POST)
        if form.is_valid():
            langue = form.save()
            #  client.user_type = "C"
            #  client.set_password(request.POST.get('password'))
            langue.save()
            return redirect('langues')  # Redirect to a view displaying the list of clients
    else:
        form = langueForm()

    return render(request, 'new_langue.html', {'form': form})


# mise a jour langue
class Editlangue(UpdateView):
    model = Language
    template_name = 'update_langue.html'
    form_class = EditlangueForm
    success_url = reverse_lazy('langues')

    def form_valid(self, form):
        pk = self.kwargs['pk']
        langue = get_object_or_404(Language, pk=pk)
        form.save()
        messages.success(self.request, 'langue  edited successfully.')
        return super().form_valid(form)

class Etudiants(ListView):
    model = User
    context_object_name = "etudiants"
    template_name = "etudiants.html"
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get("q")
        queryset = User.objects.all()
        if q != None:
            queryset = queryset.filter(Q(username__icontains=q) | Q(phone_number__icontains=q))
        return queryset

def createEtudiant(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            etudiant = form.save()
            #  client.user_type = "C"
            #  client.set_password(request.POST.get('password'))
            etudiant.save()
            return redirect('etudiants')  # Redirect to a view displaying the list of clients
    else:
        form = UserForm()

    return render(request, 'new_etudiant.html', {'form': form})

class Edituser(UpdateView):
    model = User
    template_name = 'update_etudiant.html'
    form_class = EditUserForm
    success_url = reverse_lazy('etudiants')

    def form_valid(self, form):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        form.save()
        messages.success(self.request, 'Etudiants  edited successfully.')
        return super().form_valid(form)


def DeleteEtudiant(request, pk):
    model = User
    etudiant = User.objects.filter(id=pk)
    etudiant.delete()
    # template_name = 'delete_user.html'
    messages.success(request, 'etudiant  deleted successfully.')
    return redirect('etudiants')
