from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
import random

# Create your views here.
def index(request):
    ltable = locationtable.objects.all()
    return render(request, "index.html", {"ltable": ltable})


def login(request):
    if request.method == 'POST':
        username = request.POST['un']
        firstname = request.POST['FN']
        lastname = request.POST['LN']
        password = request.POST['password']
        cpassword = request.POST['confirmpass']
        email = request.POST['email']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exists')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Exists')
                return redirect('/')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password,  first_name=firstname, last_name=lastname)
                user.save()
                print('User created')
                return redirect('/')
        else:
            messages.info(request, 'Password does not match')
            return redirect('/')


    else:
        return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['un']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            print("logged in")
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')
    else:
        return render(request, 'login.html')
        

def logout(request):
    auth.logout(request)
    print("logged out")
    return redirect('/')

def productlist(request, city):
    if (request.method == 'POST'):
        loc = request.POST.getlist('locations')
        bhk = request.POST.getlist('BHK')
        area = request.POST.getlist('area')
        actions= request.POST.getlist('actions')
        others= request.POST.getlist('others')

        lochouses = housenumber.objects.filter(location__in=loc) |  housenumber.objects.filter(bhk__in=bhk) |  housenumber.objects.filter(sqfeet__in=area) |  housenumber.objects.filter(action__in=actions) |  housenumber.objects.filter(others__in=others)
        return render(request, "productlist.html", {"lochouses": lochouses})

    lochouses = housenumber.objects.filter(location=city)
    return render(request, "productlist.html", {"lochouses": lochouses})

def product(request, hid):
    index1=index2=0
    while(index1==index2):
        random.seed()
        queryset=images.objects.all()
        index1,index2=random.sample(range(0,queryset.count()),2)
    houseimage1=queryset[index1]
    houseimage2=queryset[index2]
    print(houseimage1,houseimage2)
    houseid = housenumber.objects.filter(houseid=hid).first()

    return render(request, "product.html", {"houseimage1": houseimage1,"houseimage2": houseimage2,"houseid":houseid})

def about(request):
    return render(request, "about_us.html")
