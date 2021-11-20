from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm,InfoForm
from .models import *

# Create your views here.

def home(request):
	return render(request, 'accounts/dashboard.html')

def products(request):
	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/products.html',context)

def customer(request):
	customer = Customer.objects.all()
	return render(request, 'accounts/customer.html',{'customer':customer})




def register(request):
	form = InfoForm()
	if request.method == 'POST':
		form = InfoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/register.html',context)



def registerInfo(request):
	info = Info.objects.all()
	return render(request, 'accounts/registerInfo.html',{'info':info})


def underweight(request):
	
	return render(request, 'accounts/underweight.html')
	
	
def overweight(request):
	return render(request, 'accounts/overweight.html')