# from django.template import loader

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    latest = Question.objects.order_by('-pub_date')[:5]
    context = {'latest': latest}
    return render(request, 'poll_app/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'poll_app/detail.html', context)


def results(request, question_id):
    response = "Question %s results: "
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"Vote on question {question_id}")
