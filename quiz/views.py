from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  if request.method == 'POST':
    return HttpResponse(request.POST['add_box'])
  return render(request, 'home.html')
