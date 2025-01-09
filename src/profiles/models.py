from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from .utils import get_random_string
from analytics.models import ExperimentCondition


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    bio = models.TextField(default="", max_length=500, blank=True)
    avatar = models.ImageField(default='avatar_default.png', upload_to='profile_pictures')
    slug = models.SlugField(unique=True, blank=True)
    condition = models.ForeignKey(ExperimentCondition, on_delete=models.SET_NULL, null=True, blank=True)  # Verknüpfung zu condition
    
    def __str__(self):
        return f"{self.user.username}"

    def get_absolute_url(self):
        return reverse("profiles:profile-detail-view", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # Automatically generate or normalize slug
        if not self.slug:
            base_slug = slugify(self.user.username)
            slug = base_slug
            # Ensure unique slug
            while Profile.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{get_random_string()}"
            self.slug = slug
        else:
            # Ensure existing slug is always in lowercase
            self.slug = slugify(self.slug)
        
        super().save(*args, **kwargs)