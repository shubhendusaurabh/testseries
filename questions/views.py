from django.shortcuts import render

from django.db.models import Count
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from rest_framework import viewsets
from .serializers import QuestionSerializer, ChoiceSerializer, ExamSerializer, UnitSerializer, ChapterSerializer, SubjectSerializer

from .models import Question, Choice, Exam, Unit, Chapter, Subject

class QuestionDetail(DetailView):
    model = Question
question_detail = QuestionDetail.as_view()

class QuestionList(ListView):
    model = Question
question_list = QuestionList.as_view()

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
