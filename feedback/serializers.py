from rest_framework import serializers
from .models import FeedBack, BugReport


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'
        read_only_fields = ('feedback_provider', 'date_posted')


class ReportBugSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugReport
        fields = '__all__'
        read_only_fields = ('bug_reporter', 'date_posted')
