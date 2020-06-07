# from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

def index(request):
	latest = Question.objects.order_by('-pub_date')[:5]
	output = '<br>'.join([f'{q.question_text} {q.pub_date}' for q in latest])
	return HttpResponse(output)

def detail(request, question_id):
	return HttpResponse("Question %s: " % question_id)

def results(request, question_id):
	response = "Question %s results: "
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse(f"Vote on question {question_id}")		
