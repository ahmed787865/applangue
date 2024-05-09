from rest_framework import serializers
from .models import Teacher, Language


class TeacherSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    phone = serializers.CharField(source='phone_number')
    language = serializers.SlugRelatedField(slug_field='name', queryset=Language.objects.all())
    joined = serializers.ReadOnlyField()

    def create(self, validated_data):
        """
        Create and return a new `Teacher` instance, given the validated data.
        """
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Teacher` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'phone', 'language', 'joined')


class LanguageSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Teacher` instance, given the validated data.
        """
        return Language.objects.create(**validated_data)

    class Meta:
        model = Language
        fields = ('id', 'name')
