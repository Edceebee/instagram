from django.conf.urls.static import static
from django.urls import path

from Instagram import settings
from picsApp.views import home

urlpatterns = [
    path('', home, name='home')


]

