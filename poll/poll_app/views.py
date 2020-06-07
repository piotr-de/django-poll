# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    latest = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('poll_app/index.html')
    context = {
        'latest': latest,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("Question %s: " % question_id)


def results(request, question_id):
    response = "Question %s results: "
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"Vote on question {question_id}")
