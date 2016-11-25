import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created = models.DateTimeField('creation date', auto_now_add=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    created = models.DateTimeField('creation date', auto_now_add=True)
    last_vote_date = models.DateTimeField('last vote date', auto_now=True)

    def __str__(self):
        return self.choice_text

class Tip(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tip_text = models.TextField()

    def __str__(self):
        return self.tip_text

