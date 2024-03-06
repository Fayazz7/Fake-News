from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    profile_pic = models.ImageField(
        upload_to="profileimages", default="profile.jpg", null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    options = (
        ("male", "male"), ("female", "female")
    )
    gender = models.CharField(max_length=200, choices=options, default="male")
    about = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class UserRequest(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="request")
    text = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    options = (
        ("pending", "pending"), ("approved", "approved"), ("rejected", "rejected")
    )
    status = models.CharField(
        max_length=200, choices=options, default="pending", blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.owner.username
