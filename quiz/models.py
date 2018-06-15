from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=100)
    yes_answer = models.BooleanField("Yes")
    no_answer = models.BooleanField("No")

    def __str__(self):
        return self.question
