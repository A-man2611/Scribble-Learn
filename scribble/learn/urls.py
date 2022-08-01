from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name ='home'),
    path('Alphabet_Recognizer', views.Alphabet_Recognizer, name ='Alphabet_Recognizer'),
    path('Emojinator', views.Emojinator, name ='Emojinator'),
    path('Rock_paper_scissors', views.Rock_paper_scissors, name ='Rock_paper_scissors')
]