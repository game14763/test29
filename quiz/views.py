from django.shortcuts import render
from django.http import HttpResponse
from quiz.forms import QuizForm
from quiz.models import Quiz

def index(request):
  add_form = QuizForm()
  new_form = ''
  if request.method == 'POST':
    new_form = QuizForm(request.POST)
    if new_form.is_valid():
        new_form.save(commit=True)
    else:
        print('ERROR FORM INVALID')
  return render(request, 'quiz/home.html', {'add_form':add_form})

def start(request):
    quiz_list = Quiz.objects.all()
    your_answer = ''
    quiz_id = ''
    if request.method =="POST":
        quiz_id = request.POST.get('q_id')
        if request.POST.get('yesbox', 'off') == 'on':
            your_answer = True
        elif request.POST.get('nobox', 'off') == 'on':
            your_answer = False
    quiz_dict = {'quiz_add':quiz_list, 'your_answer':your_answer, 'quiz_id':quiz_id}
    return render(request, 'quiz/start.html',context=quiz_dict)
