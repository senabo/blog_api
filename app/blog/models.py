from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    """Post model"""

    title = models.CharField(max_length=120, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField(User, related_name="votes_set", blank=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment model"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"By {self.author} on {self.post}: {self.content} "
