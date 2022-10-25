from django.urls import path
from .views import SurveyView, SurveyQuestionView, QuestionAlternativeView


urlpatterns = [
    path('survey/', SurveyView.as_view(), name='survey'),
    path('question/', SurveyQuestionView.as_view(), name='question'),
    path('alternative/', QuestionAlternativeView.as_view(), name='alternative')
]
