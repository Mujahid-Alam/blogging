from django.urls import include, path
from .views import *


urlpatterns = [
    path('', home),
    path('about/', about),

    path('post/<slug:url>', urlpost),
    path('category/<slug:url>', category),


]

