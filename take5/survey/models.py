from django.db import models

# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    creation_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'survey'

class SurveyQuestion(models.Model):
    question = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(Survey , on_delete=models.CASCADE)

    class Meta:
        db_table = 'survey_question'

class SurveyQuestionAlternative(models.Model):
    name = models.CharField(max_length=100)
    alternative = models.IntegerField()
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'survey_question_alternative'


class SurveyUserAnswer(models.Model):
    response = models.IntegerField(null=True)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'survey_user_answer'

