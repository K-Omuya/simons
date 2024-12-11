from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Member


# Create your views here.

def index(request):
    return render(request, 'index.html')
    # if request.method == 'POST':
    #     if Member.objects.filter(
    #             email=request.POST['email'],
    #             username=request.POST['username'],
    #             password=request.POST['password']
    #     ).exists():
    #         member = Member.objects.get(
    #             email=request.POST['email'],
    #             username=request.POST['username'],
    #             password=request.POST['password'],
    #         )
    #         return render(request, 'index.html', {'members': member})
    #         return redirect('index')
    #     else:
    #         return render(request, 'login.html')
    # else:
    #     return render(request,'login.html')


def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')

def faq(request):
    return render(request,'faq.html')

def blog(request):
    return render(request,'blog.html')

def cart(request):
    return render(request,'cart.html')
def track(request):
    return render(request,'track.html')

def categories(request):
     render(request,'categories.html')


def register(request):
        if request.method == "POST":
            members = Member(
                email=request.POST['email'],
                username=request.POST['username'],
                password=request.POST['password']
            )
            members.save()
            return redirect('/index')
        else:
            return render(request, 'register.html')


def login(request):
    render(request, 'login.html')