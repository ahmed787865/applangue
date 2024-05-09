from django.urls import path

from teachers import viewsets

urlpatterns = [
    path('teachers/', viewsets.TeachersViewSet.as_view(), name='teachers'),
    path('teachers/<uuid:pk>/', viewsets.TeacherDetailViewSet.as_view(), name='teacher-detail'),
    path('languages/', viewsets.LanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='languages'),
]

































