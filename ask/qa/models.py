from  django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateField()
  rating = models.IntegerField()
  author = models.CharField(max_length=100)
  likes = models.ManyToManyField(User)
  
class Answer(midels.Model):
  text = models.TextField()
  added_at = models.DateField()
  question = models.OneToOneField(Question)
  author = User

class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')
