
from django.urls import path

from teachers import viewsets
#from .viewsets import login_view, TeacherByLanguageViewSet
from .views import home, logout_view, Allteachers, createTeacher, Editteacher, DeleteTeacher, \
    teacher_details, langues, DeleteLangue, createLangue, Editlangue, LoginView, Etudiants, Edituser, createEtudiant, \
    DeleteEtudiant

urlpatterns = [
    path('teachers/', viewsets.TeachersViewSet.as_view(), name='teachers'),
    path('teachers/language/<uuid:langueId>/', viewsets.TeachersByLangauge, name='teachers-by-language'),
    path('teachers/<uuid:pk>/', viewsets.TeacherDetailViewSet.as_view(), name='teacher-detail'),
    path('languages/', viewsets.LanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='languages'),

    #######login#####
    path('', home ,name='home'),
    path('logout', logout_view, name='logout_view'),
    path('accounts/login/', LoginView.as_view(), name='login'),

    #########dashboard###########

    path('Enseignants/', Allteachers.as_view(), name='Enseignants'),
    path('teacher/new', createTeacher, name='new_teacher'),
    path('teacher/edit/<str:pk>/', Editteacher.as_view(), name='edit_teacher'),
    path('teacher/delete/<str:pk>/', DeleteTeacher ,name='delete_teacher'),
    path('teacher/<str:pk>/', teacher_details, name='teacher_details'),
    #########EtudiantS######
    path('etudiants/', Etudiants.as_view(), name='etudiants'),
    path('etudiant/edit/<str:pk>/', Edituser.as_view(), name='edit_etudiant'),
    path('etudiant/new', createEtudiant, name='new_etudiant'),
    path('etudiant/delete/<str:pk>/', DeleteEtudiant, name='delete_etudiant'),

    path('langues/', langues.as_view(), name='langues'),
    path('langue/delete/<str:pk>/', DeleteLangue, name='delete_langue'),
    path('langue/new', createLangue, name='new_langue'),
    path('langue/edit/<str:pk>/', Editlangue.as_view(), name='edit_langue'),

]


































