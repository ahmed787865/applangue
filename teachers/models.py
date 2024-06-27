import uuid

from django.db import models


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, unique=True, null=False, blank=False)
    language = models.ForeignKey('Language', on_delete=models.PROTECT, related_name='teachers', null=False)
    niveau_etude = models.CharField(max_length=100, null=False, blank=False)
    experience = models.CharField(max_length=100, null=False, blank=False)
    joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teachers'
        ordering = ['joined']


class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'languages'
        ordering = ['name']

    def __str__(self):
        return self.name
