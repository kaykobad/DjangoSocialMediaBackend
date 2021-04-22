from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import FeedBack, BugReport
from .serializers import FeedBackSerializer, ReportBugSerializer


class FeedBackViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]

    @action(methods=['POST', ], detail=False, url_path='post-feedback', permission_classes=[IsAuthenticated, ])
    def post_feedback(self, request):
        serializer = FeedBackSerializer(data=request.data)
        if serializer.is_valid():
            FeedBack.objects.create(
                feedback_provider=request.user,
                feedback=serializer.validated_data['feedback'],
                rating=serializer.validated_data['rating']
            )
            data = {'detail': 'Success! Thanks for your feedback. Your feedback has been sent to the authority.'}
        else:
            print(serializer.errors)
            data = {'detail': 'Error! Something went wrong. Please try again later.'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='report-bug', permission_classes=[IsAuthenticated, ])
    def report_bug(self, request):
        serializer = ReportBugSerializer(data=request.data)
        if serializer.is_valid():
            BugReport.objects.create(
                bug_reporter=request.user,
                bug_information=serializer.validated_data['bug_information']
            )
            data = {'detail': 'Success! Thanks for reporting the issue. Your concern has been sent to the authority.'}
        else:
            print(serializer.errors)
            data = {'detail': 'Error! Something went wrong. Please try again later.'}
        return Response(data=data, status=status.HTTP_200_OK)
