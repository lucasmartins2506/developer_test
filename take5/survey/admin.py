from django.contrib import admin
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer
# Register your models here.

my_models = [Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer]
admin.site.register(my_models)


