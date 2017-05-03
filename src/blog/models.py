from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
# Create your models here.
def validate_content(value):
    content = value
    if content == 'fuck':
        raise ValidationError("Watch your language")
    return value


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return str(self.tag_name)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100,unique=True,validators=[validate_content])
    subtitle = models.CharField(max_length=100,null=True)
    content = models.TextField(max_length = 5000)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.title)






class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField(max_length = 200)
    timestamp = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content
