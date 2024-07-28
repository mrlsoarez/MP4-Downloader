from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm, NameForm2
import os

##########################
from pytubefix import YouTube

yt = None
def get_link(request):
    global yt
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            yt = YouTube(link) 
            options = []
            try:
                for obj in yt.streams:
                    options.append((str(obj.itag), obj))
                form = NameForm2(choices=options)
                form.fields['my_field'].choices = options
                return render(request, "dir/main.html", {"img": yt.thumbnail_url, "link_found": True, "form": form})

            except Exception as e:
                print("Error:", e)       
    else:
        form = NameForm()

    return render(request, "dir/main.html", {"form": form})

def download(request):
    print(yt, 'link')
    def get_download_folder():
        home_directory = os.path.expanduser('~')  # Obtém o diretório home do usuário
        downloads_folder = os.path.join(home_directory, 'Downloads')
        return downloads_folder
    
    if (request.method == 'POST'):
        form = NameForm2(request.POST)
        tag = form['my_field'].value()
        stream = yt.streams.get_by_itag(tag)
        folder = get_download_folder()
        stream.download(folder, yt.title)
        
    return HttpResponse("Eu to fenol")






