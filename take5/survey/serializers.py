from rest_framework import serializers
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            'name',
            'description',
            'creation_date'
        )


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = (
            'question',
            'creation_date',
            'survey'
        )


class QuestionAlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAlternative
        fields = (
            'name',
            'alternative',
            'survey_question'
        )
