from django.db import models

class FeedbackData(models.Model):
    name = models.CharField(max_length=30)
    ramnaamjap = models.IntegerField()
    feedback_date = models.DateTimeField(auto_now_add=True)
