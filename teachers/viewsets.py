from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from teachers.models import Teacher, Language
from teachers.serializers import TeacherSerializer, LanguageSerializer
from users.permissions import IsStaffForPost

from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.decorators import api_view


class TeachersViewSet(APIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsStaffForPost]
    authentication_classes = [JWTAuthentication]


    @staticmethod
    def post(request, *args, **kwargs):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        return Response(TeacherSerializer(teacher).data, status=status.HTTP_201_CREATED)

    @staticmethod
    def get(self, pk=None, language=None):  # Add 'language' argument
        if pk:
            # Handle retrieving a specific teacher by ID (if applicable)
            teacher = Teacher.objects.get(pk=pk)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
        elif language:
            # Handle retrieving teachers by language
            teachers = Teacher.objects.filter(languages__icontains=language)
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)
        else:
            # Handle retrieving all teachers (optional)
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)


class TeacherDetailViewSet(APIView):
    @staticmethod
    def get(request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise NotFound('Teacher with ID %s not founddd' % pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)


@api_view(['GET'])
def TeachersByLangauge(request, langueId):
        try:
            teachers = Teacher.objects.filter(language_id=langueId)
        except Teacher.DoesNotExist:
            raise NotFound('Teacher with langueID %s not found' % langueId)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


class LanguagesViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    permission_classes = [IsStaffForPost]
    authentication_classes = [JWTAuthentication]
    queryset = Language.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        language = serializer.save()
        return Response(LanguageSerializer(language).data, status=status.HTTP_201_CREATED)


class listelangue(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    permission_classes = [IsStaffForPost]
    authentication_classes = [JWTAuthentication]

    # queryset = Language.objects.all()

    def list(self):
        queryset = Language.objects.all();
        return queryset


class teachers(ListView):
    model = Teacher
    context_object_name = "teacher"
    template_name = "teachers/teacher_list.html"
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get("q")
        queryset = Teacher.objects.all()
        return queryset


class TeacherLanguageListViewset(viewsets.ModelViewSet):
    def get(self, request, language):
        teachers = Teacher.objects.filter(
            languages__icontains=language)  # Filter by language (adjust based on your model)
        serializer = TeacherSerializer(teachers, many=True)  # Replace with your serializer class
        return Response(serializer.data)


class login_view(APIView):
    def post(self, request):
        if request.method == 'POST':
            return 'login.html',
