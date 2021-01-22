from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(username= username, password= password)

        if user:
            #Check if user is activate
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            return HttpResponse('Invalid login details')

    else:
        return render(request, 'login.html', {})
