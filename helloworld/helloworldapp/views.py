from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello (request):
	return HttpResponse("hello welcome to the world of django framework")
