from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
  add_form = forms.QuizForm()
  new_question = ''
  if request.method == 'POST':
    new_question = forms.QuizForm(request.POST)
    print("Question Add")
  return render(request, 'quiz/home.html', {'add_form':add_form, 'new_question':new_question, })

def start(request):
    return render(request, 'quiz/start.html')
