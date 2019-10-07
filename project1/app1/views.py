from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func1(request):
	return render(request,'first.html',{'cool':'add'})

def add(request):

	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])
	res = val1 + val2

	return render(request,"result.html",{'result':res})
