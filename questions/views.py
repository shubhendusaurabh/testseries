from django.shortcuts import render

from django.db.models import Count
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from .models import Question, Choice

class QuestionDetail(DetailView):
    model = Question
question_detail = QuestionDetail.as_view()

class QuestionList(ListView):
    model = Question
question_list = QuestionList.as_view()
