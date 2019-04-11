from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog

# Create your models here.
class Comment(models.Model):
    to_blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering=('-comment_time',)