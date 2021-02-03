from django.shortcuts import render
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
            #Check if user exists

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

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('accounts/templates/registration/acc_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

                #return HttpResponseRedirect(reverse('accounts:login'))
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
