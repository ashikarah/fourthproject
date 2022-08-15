from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth.models import User
from django.shortcuts import render, redirect


@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passsw = request.POST['password']
        user=auth.authenticate(username=username,password=passsw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid .....')
    return render(request,'login.html')
def register(request):


    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        passw = request.POST['psw']
        rpassw = request.POST['psw-repeat']

        if passw == rpassw:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username tacken')
                return  redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is tacken')
                return  redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=passw)
                user.save()
                messages.info(request, 'successfully registeredddd......')
                return redirect(login)
        else:
            messages.info(request, 'Unable to register......')
            return redirect(register)

    return render(request, 'register.html')
