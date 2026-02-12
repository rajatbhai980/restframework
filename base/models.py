from django.db import models
import datetime 
from django.utils import timezone
# Create your models here.
class Question(models.Model): 
    question = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.question
    
    

class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self): 
        return self.choice_text