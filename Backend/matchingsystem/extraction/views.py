from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import Lecturer

# Create your views here.
def upload(request):
    context= {}
    if request.method== 'POST':
        uploaded_file= request.FILES["document"]

        #Save file
        fs= FileSystemStorage()
        name= fs.save(uploaded_file.name, uploaded_file)
        context['url']= fs.url(name)

    return render(request, 'upload.html', context)


def upload_document(request):
    '''
        Uploads documents
    '''

    if request.method == 'POST':

        #Obtain the file sent
        form = DocumentForm(request.POST, request.FILES)
        print(form)

        #Check if all details are valid
        if form.is_valid():
            #Save the file
            form= form.save(commit=False)

            #Get user
            user= request.user
            form.author= Lecturer.objects.get(user=user)
            form.save()
            print("Saved successfully")
            return redirect("extraction:upload")
        # return HttpResponse("Post executing")
    # else:
    #     form = DocumentForm()
    #     return render(request, 'upload_document.html', {
    #     'form': form
    # })
