from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect

from picsApp.forms import InstagramForm
from picsApp.models import Photo


def home(request):
    if request.method == "POST":
        form = InstagramForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            # return redirect('home')

    photos = Photo.objects.all()
    context = {'photos': photos, 'form': InstagramForm()}
    return render(request, 'picsApp/home.html', context)

