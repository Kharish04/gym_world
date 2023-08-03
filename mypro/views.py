from django.shortcuts import render
from django.shortcuts import render , redirect
from mypro.forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 

def register(request):	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('appname:login_reg')


	context = { 'form': form }
	return render (request, 'signin/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('appname:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'signin/login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('appname:login_reg')


@login_required(login_url = 'appname:login_reg')
def info(request):
	return render (request,"signin/info.html", context = {})
# Create your views here.
def home(request):
    return  render(request,'home.html')
def about(request):
    return  render(request,'about.html')
def blog_single(request):
    return  render(request,'blog_single.html')
def blog(request):
    return  render(request,'blog.html')
def contact(request):
    return  render(request,'contact.html')
def index(request):
    return  render(request,'index.html')
def portfolio(request):
    return  render(request,'portfolio.html')

def submit(request):
    a = request.POST(['initial'])
    return render(request, 'home/home.html', {
        'error_message': "returned"
    })
