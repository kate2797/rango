from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    NAME_MAX_LENGTH = 128  # Class variable to avoid repetition of fixed values
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # Required. Links UserProfile to a User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include
    # Form can be submitted without a website field or picture
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
