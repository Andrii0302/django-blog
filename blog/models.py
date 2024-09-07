from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    captions=models.CharField(max_length=20)
    def __str__(self):
        return self.captions
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_address=models.EmailField()
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return self.full_name
class Post(models.Model):
    title=models.CharField(max_length=150)
    excerpt=models.CharField(max_length=200)
    image=models.ImageField(upload_to='posts',null=True)
    author=models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts',null=True)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(max_length=200,unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    user_name=models.CharField(max_length=120)
    user_email=models.EmailField()
    text=models.TextField(max_length=400)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
