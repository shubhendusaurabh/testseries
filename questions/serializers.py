from rest_framework import serializers

from .models import Question, Choice, Exam, Subject, Unit, Chapter

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = serializers.StringRelatedField(many=True)
    class Meta:
        model = Question
        fields = ('pk', 'question_text', 'answer', 'chapter', 'image', 'choices')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text', 'question')

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = ('name', 'abbr', 'description')

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', )

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ('name', 'subject')

class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('name', 'unit')
