from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()


class FeedBack(models.Model):
    feedback_provider = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='feedback')
    feedback = models.TextField()
    rating = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback + " - Rating: " + str(self.rating)

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "All Feedback"


class BugReport(models.Model):
    bug_reporter = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='bug')
    bug_information = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bug_reporter.first_name + " - Bug: " + self.bug_information

    class Meta:
        verbose_name = "Bug Report"
        verbose_name_plural = "Bug Reports"
