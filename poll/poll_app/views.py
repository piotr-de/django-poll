# from django.template import loader

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'poll_app/index.html'
    context_object_name = 'latest'

    def get_queryset(self):
        """Return the last 5 questions"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.ListView):
    model = Question
    template_name = 'poll_app/detail.html'


class ResultsView(generic.ListView):
    model = Question
    template_name = 'poll_app/results.html'


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
