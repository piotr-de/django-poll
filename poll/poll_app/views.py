# from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


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
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll_app/detail.html', {
            'question': question,
            'error_message': "Please select one of the options.",
        })
    else:
        selected.votes += 1
        selected.save()
        return HttpResponseRedirect(
            reverse('poll_app:results', args=(question_id,))
        )
