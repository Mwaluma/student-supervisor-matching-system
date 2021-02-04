from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib import messages

##################################################################################

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('accounts/dashboard')
    else:

        form= CreateUserForm()

        if request.method == 'POST':
            form= CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('accounts:login')

        context= {'form': form}
        return render(request, 'registration/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            print(user)
            return redirect('accounts:dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context= {}
    return render(request, 'registration/login.html', context )

def logoutUser(request):
    logout(request)
    return redirect('accounts:login')


###############################################################################

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        #Checks for user and returns the user object
        user= authenticate(request, username= username, password= password)


        if user is not None:
            #Check if user is active
            if user.is_active:
                #Attaches the user to the current session
                login(request, user)
                return redirect('accounts:dashboard')

            else:
                #Display user not active
                messages.info(request, 'USER IS NOT ACTIVE')

        else:
            #Display failed authentication
            messages.info(request, 'Username or Password is incorrect')


    context= {}
    return render(request, 'registration/logintest.html', context)


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
            user.is_active= False
            user.save()
            #user.set_password(user.password)
            #user.save()

            lecturer= lecturer_form.save(commit=False)
            lecturer.user = user
            lecturer.save()

            profile= profile_picture_form.save(commit=False)
            profile.lecturer= lecturer
            profile.save()

            user= user_form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)


            # current_site = get_current_site(request)
            # mail_subject = 'Activate your account.'
            # message = render_to_string('registration/acc_activate_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #     mail_subject, message, to=[to_email]
            # )
            # email.send()
            return redirect('accounts:login')

    #Create forms to be rendered
    user_form= forms.UserForm()
    lecturer_form= forms.LecturerForm()
    profile_picture_form= forms.LecturerProfilePictureForm()
    return render(request, 'registration/registration.html', {'user_form': user_form, 'lecturer_form': lecturer_form, 'profile_picture_form': profile_picture_form} )


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def dashboard(request):
    return render(request, "dashboard.html")
