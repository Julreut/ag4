from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from .utils import get_random_string


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    bio = models.TextField(default="", max_length=500, blank=True)
    avatar = models.ImageField(default='avatar_default.png', upload_to='profile_pictures')
    slug = models.SlugField(unique=True, blank=True)
    condition_id = models.IntegerField(null=True, blank=True)  # Versuchsbedingungs-ID



    def __str__(self):
        return f"{self.user.username}"

    def get_absolute_url(self):
        return reverse("profiles:profile-detail-view", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # Automatically generate slug if not present
        if not self.slug:
            base_slug = slugify(self.user.username)
            slug = base_slug
            # Ensure unique slug
            while Profile.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{get_random_string()}"
            self.slug = slug
        super().save(*args, **kwargs)
