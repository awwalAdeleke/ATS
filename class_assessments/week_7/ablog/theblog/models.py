from ckeditor.fields import RichTextField       # type: ignore
from datetime import datetime, time

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(is_deleted=False)

class DeletedManager(models.Manager):
    def get_queryset(self):
        queryset = super(DeletedManager, self).get_queryset()
        return queryset.filter(is_deleted=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', kwargs={'pk': self.pk})
        return reverse('home')


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255)
    # body = models.TextField()
    category = models.CharField(max_length=100, default='coding') # coding, entertainment, normal stuff, hiking and general.
    post_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = models.Manager()
    active_posts = ActiveManager()
    deleted_posts = DeletedManager()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', kwargs={'pk': self.pk})
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    objects = models.Manager()
    active_comments = ActiveManager()
    deleted_comments = DeletedManager()


    def __str__(self):
        return f"{self.post.title} - {self.name}"
    
    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})