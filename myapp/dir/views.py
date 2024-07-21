from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

##########################
from pytube import YouTube

def get_link(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            link = form.cleaned_data['link']
            yt = YouTube(link)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print("=========", link)
            return render(request, "dir/sucess.html", {"img": yt.thumbnail_url})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "dir/main.html", {"form": form})



