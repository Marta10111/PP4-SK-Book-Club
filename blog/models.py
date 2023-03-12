from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Model for Post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    location = models.CharField(max_length=50)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="location_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        Posts ordered to show newest post first
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def number_of_likes(self):
        """
        Returns number of likes for post
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Model for Comment
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    """
    Comments odered to show oldest to newest
    """
    ordering = ['created_on']


def __str__(self):
    return f"Comment {self.body} by {self.name}"