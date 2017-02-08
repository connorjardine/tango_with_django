from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner! <br/> Click <a href='/rango/about/'> here</a> to go to the about page")
	
def about(request):
	return HttpResponse("This is the about page <a href='/rango/'>Index</a>")
