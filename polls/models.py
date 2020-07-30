import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    portofolio_site = models.URLField(blank = True)
    profile_pic = models.Imagefield(upload_to = 'profile_pics', blank = True)
    def __str__(self):
        return self.user.username


