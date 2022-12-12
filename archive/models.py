from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

TUNE_TYPE = (
    ('Jig', 'Jig'),
    ('Hornpipe', 'Hornpipe'),
    ('Reel', 'Reel'),
    ('Polka', 'Polka'),
    ('Setdance', 'Setdance'),
    ('Slip Jig', 'Slip Jig'),
    ('Slow Air', 'Slow Air'),
    ('Barndance', 'Barndance'),
)

# Create your models here.


class Tune(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="archive_posts", null=True
    )
    title = models.CharField(max_length=200, unique=True)
    tune_type = models.CharField(
        max_length=9, choices=TUNE_TYPE, default='Jig')
    composer = models.CharField(max_length=200, unique=True)
    learned_from = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='tune_like', blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Tune, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
