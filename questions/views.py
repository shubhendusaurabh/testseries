from datetime import datetime, timedelta

from django.shortcuts import render

from django.db.models import Count
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import QuestionSerializer, ChoiceSerializer, ExamSerializer, UnitSerializer, ChapterSerializer, SubjectSerializer

from .models import Question, Choice, Exam, Unit, Chapter, Subject

class QuestionDetail(DetailView):
    model = Question
question_detail = QuestionDetail.as_view()

class QuestionList(ListView):
    model = Question
question_list = QuestionList.as_view()

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class ChapterViewSet(ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class TestDateTime(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        endtime = datetime.now() + timedelta(hours=3)
        content = {'endtime': endtime}
        return Response(content)
