from django.urls import include, path
from .views import *


urlpatterns = [
    path('', home),
    path('about/', about),
    path('login/', login),
    path('signup/', signup),
    path('logout/', logout),


    path('post/<slug:url>', urlpost),
    path('category/<slug:url>', category),


]

