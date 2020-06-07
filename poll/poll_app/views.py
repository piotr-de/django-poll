# from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world")

def detail(request, question_id):
	return HttpResponse("Question %s:" % question_id)

def results(request, question_id):
	response = "Question %s results:"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse(f"Vote on question {question_id}")		
