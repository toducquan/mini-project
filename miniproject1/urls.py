from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^myapp/', include('myapp.urls')) #set up router 'myapp/'
]
