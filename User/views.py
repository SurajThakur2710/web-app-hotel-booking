from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def forgotPassword(request):
    return render(request, 'Forgot Password.html')


# def Login(request):
#     return render(request, 'login/login.html')

def signup(request):
    # new_user = User.

    if request.method == 'POST':

  
        first_name = request.POST['first_name']
       
        email = request.POST['email']
        # password = request.POST['phone']
        password = request.POST['password']
        username = request.POST["username"]
        newuser = User.objects.create_user(username=username , password = password, email=email,first_name= first_name) 
        newuser.save()
        messages.success(request, 'Profile Created. Login Please.')
        return render(request, 'login/login.html')

        # return redirect('/')

    else:
        # return HttpResponse('Error')
        return render(request, 'Signup.html')
    


def Login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['psw']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,'username or password not correct. Please login Again')
                return render(request, 'login/login.html')
        else:
            return render(request, 'login/login.html')
