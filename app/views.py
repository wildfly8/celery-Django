from django.shortcuts import render
from django.http import HttpResponse
from app.tasks import hello

# Create your views here.
def test_celery(request):
    return HttpResponse(hello())
