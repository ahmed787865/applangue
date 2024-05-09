from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from teachers.models import Teacher, Language
from teachers.serializers import TeacherSerializer, LanguageSerializer
from users.permissions import IsStaffForPost

from django.views.generic import ListView


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
    def get(request):
        language_name = request.query_params.get('language')
        if language_name:
            teachers = Teacher.objects.filter(language__name=language_name)
        else:
            teachers = Teacher.objects.all()

        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherDetailViewSet(APIView):
    @staticmethod
    def get(request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise NotFound('Teacher with ID %s not found' % pk)
        serializer = TeacherSerializer(teacher)
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


class teachers(ListView):
    model = Teacher
    context_object_name = "teacher"
    template_name = "teachers/teachers.html"
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get("q")
        queryset = Teacher.objects.all()
        return queryset
