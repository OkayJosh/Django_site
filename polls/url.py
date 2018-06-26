""" Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home') """
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #example: /polls/
    path('', views.index, name='index'),
    #example: /polls/5
    path(r'<int:question_id>/', views.detail, name='detail'),
    #example: /polls/5/results/
    path(r'<int:question_id>/results/', views.results, name='results'),
    #example: /polls/5/vote/
    path(r'<int:question_id>/vote/', views.vote, name='vote'),
]