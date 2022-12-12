from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    short_intro = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True,
                                      upload_to='profiles/',
                                      default='profiles/user-default.png')
    social_github = models.CharField(max_length=255, blank=True, null=True)
    social_twitter = models.CharField(max_length=255, blank=True, null=True)
    social_linkedin = models.CharField(max_length=255, blank=True, null=True)
    social_youtube = models.CharField(max_length=255, blank=True, null=True)
    social_website = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                               null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                  null=True, blank=True,
                                  related_name='messages')
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']
