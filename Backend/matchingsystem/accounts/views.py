from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from . import forms

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

def lecturer_register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_form= forms.UserForm(data= request.POST)
        lecturer_form= forms.LecturerForm(data= request.POST)
        profile_picture_form= forms.LecturerProfilePictureForm(request.POST, request.FILES)

        #Check if the fields are valid
        if user_form.is_valid() and lecturer_form.is_valid() and profile_picture_form.is_valid():
                user= user_form.save(commit=False)
                user.username= user.email
                user.save()
                user.set_password(user.password)
                user.save()

                lecturer= lecturer_form.save(commit=False)
                lecturer.user = user
                lecturer.save()

                profile= profile_picture_form.save(commit=False)
                profile.lecturer= lecturer
                profile.save()

                return HttpResponseRedirect(reverse('accounts:login'))
        else:
            # if user_form.is_valid():
            #     return HttpResponse('{}'.format(user_form.errors))
            # elif lecturer_form.is_valid():
            #     return HttpResponse('{}'.format(lecturer_form.errors))
            # else:
            #     return HttpResponse('{}'.format(profile_picture_form.errors))
            #
            print(user_form.errors, lecturer_form.errors, profile_picture_form.errors)
            return HttpResponse("Something is wrong with the validation")

    else:
        user_form= forms.UserForm()
        lecturer_form= forms.LecturerForm()
        profile_picture_form= forms.LecturerProfilePictureForm()
        return render(request, 'registration/registration.html', {'user_form': user_form, 'lecturer_form': lecturer_form, 'profile_picture_form': profile_picture_form} )
