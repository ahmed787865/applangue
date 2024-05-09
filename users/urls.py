from django.urls import path

from . import viewsets

urlpatterns = [
    path('signup/', viewsets.SignUpViewSet.as_view(), name='signup'),
]
