from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')
def Alphabet_Recognizer(request):
    return render(request, 'Alphabet_Recognizer.html')
def Emojinator(request):
    return render(request, 'Emojinator.html')
def Rock_paper_scissors(request):
    return render(request, 'Rock_paper_scissors.html')