from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
            model = Submission
            fields = ['id', 'date', 'who', 'where', 'what']