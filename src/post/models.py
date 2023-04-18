from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.
User = get_user_model()
class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_profile = models.ImageField()

    def __str__(self) -> str:
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title
class Post(models.Model):

    title  = models.CharField(max_length=50)
    over_view = models.TextField()
    content = RichTextUploadingField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"id": self.id})
     