from django.contrib import admin
from .models import FeedBack, BugReport


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('id', 'feedback_provider', 'feedback', 'rating', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('feedback_provider__email', 'feedback_provider__first_name', 'feedback_provider__last_name', 'feedback', 'rating')
    ordering = ('id', 'feedback_provider', 'feedback', 'rating', 'date_posted')
    list_display_links = ('id', 'feedback_provider')


@admin.register(BugReport)
class ReportBugAdmin(admin.ModelAdmin):
    list_display = ('id', 'bug_reporter', 'bug_information', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('bug_reporter__email', 'bug_reporter__first_name', 'bug_reporter__last_name', 'bug_information')
    ordering = ('id', 'bug_reporter', 'bug_information', 'date_posted')
    list_display_links = ('id', 'bug_reporter')
