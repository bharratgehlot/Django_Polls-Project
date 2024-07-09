from django.db import models
from django.utils import timezone
import uuid

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  
  def __str__ (self):
    return self.question_text

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  
  def __str__ (self):
    return self.choice_text
  
class User(models.Model):
  username = models.CharField(max_length=200, unique=True, default=uuid.uuid4)  
  
  def __str__(self):
    return self.username
  
class Responses(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
  response_date =  models.DateTimeField(default=timezone.now)  
  
  def __str__(self):
    return f'{self.user} - {self.question} - {self.choice}'  