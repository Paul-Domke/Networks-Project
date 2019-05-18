from django.shortcuts import render
from django.http import HttpResponse

#These are called when certain urls are visited

def home(request):
	return render(request, 'project/home.html')

def DDOSExplained(request):
	return render(request,'project/Josh.html')

def DDOSHistory(request):
	return render(request,'project/Andrew.html')

def DDOSProtection(request):
	return render(request,'project/Chief.html')
