from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    image = models.ImageField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    kcal = models.IntegerField()
    proteins = models.IntegerField()
    fats = models.IntegerField()
    carbs = models.IntegerField()
    hashtags = models.JSONField()


class User(models.Model):
    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=256)
    

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True),
    likes = models.IntegerField(default=0)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)


class Hashtag(models.Model):
    name = models.CharField(max_length=15, unique=True)