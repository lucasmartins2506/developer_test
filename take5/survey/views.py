from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative
from .serializers import SurveySerializer, SurveyQuestionSerializer, QuestionAlternativeSerializer


class SurveyView(APIView):
    def get(self, request):
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return Response(serializer.data)


class SurveyQuestionView(APIView):
    def get(self, request):
        survey_question = SurveyQuestion.objects.all()
        serializer = SurveyQuestionSerializer(survey_question, many=True)
        return Response(serializer.data)


class QuestionAlternativeView(APIView):
    def get(self, request):
        question_alternative = SurveyQuestionAlternative.objects.all()
        serializer = QuestionAlternativeSerializer(question_alternative, many=True)
        return Response(serializer.data)
