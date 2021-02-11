from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import Lecturer
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from matchingsystem import settings
from extraction.packages.extract_text import extract_text_from_document
from extraction.packages.rake import Rake
from extraction.packages.extract_text import extract_tf
from collections import Counter, defaultdict
from django.contrib.auth.decorators import login_required

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

@csrf_exempt
@login_required(login_url='accounts:login')
def upload_document(request):
    '''
        Uploads documents
    '''

    if request.method == 'POST':

        #Obtain the file sent
        form = DocumentForm(request.POST, request.FILES)

        #Document load

        #Check if all details are valid
        if form.is_valid():
            #Save the file
            form= form.save(commit=False)

            #Get user
            user= request.user
            form.author= Lecturer.objects.get(user=user)
            form.save()
            messages.success(request, f'{request.FILES["doc"].name} has been uploaded successfuly')


            #Get the url
            url= "/".join([settings.MEDIA_DIR,str(form.doc)])

            #Extract text from document
            text= extract_text_from_document(url=url).lower()

            #Extract keywords from the document
            r= Rake()
            r.extract_keywords_from_text(text)

            keywords= r.get_ranked_phrases()

            #Get keywords as a dictionary {'keyword': tf}
            keywords= extract_tf(keywords,text)


            #Create postlist
            for term,tf in keywords.items():
                #Create postlist
                keywords[term]= [request.user.id,tf]

            #main index
            main_index= defaultdict(list)
            print(main_index)

            #Load index in memory
            f=open("/".join([settings.MEDIA_DIR,'indexfile.txt']), 'r', encoding="utf-8")
            for line in f:
                line=line.rstrip()
                term,documents= line.split('|')
                documents= documents.split(';')

                for doc in documents:
                    postings= doc.split(',')
                    main_index[term].append(postings)

            f.close()



            #Append keyword to main index
            for term,value in keywords.items():
                main_index[term].append(value)

            #Write to txt
            f=open("/".join([settings.MEDIA_DIR,'indexfile.txt']), 'w', encoding="utf-8")
            for term,value in main_index.items():
                postinglist=[]

                for p in value:
                    lecID=p[0]
                    tf=p[1]
                    postinglist.append(','.join([str(lecID), str(tf)]))

                string= ''.join((term,'|',';'.join(postinglist)))

                #write to file
                f.write(f"{string}\n")

            f.close()

            return redirect("accounts:dashboard")
        #return HttpResponse("Post executing")
    # else:
    #     form = DocumentForm()
    #     return render(request, 'upload_document.html', {
    #     'form': form
    # })
