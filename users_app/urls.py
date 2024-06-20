
from django.urls import path
from .views import RegisterView, LoginView, TeacherOnlyView, StudentOnlyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('teacher/', TeacherOnlyView.as_view(), name='teacher'),
    path('student/', StudentOnlyView.as_view(), name='student'),
]
