from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Doc
from uploads.core.forms import DocumentForm


def home(request):
    documents = Doc.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else if request.method == 'GET': # If the form is submitted

        search_query = request.GET.get('search_box', None)
	form = DocumentForm()
    	return render(request, 'core/model_form_upload.html', {
        'form': form
    })
