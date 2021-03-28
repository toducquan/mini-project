from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^library/(?P<library_id>[0-9]+)$', views.book, name = "book"),
    url(r'^book/(?P<book_id>[0-9]+)$', views.view_book, name="view_book"),
    url(r'^del/(?P<book_id>[0-9]+)$', views.del_book, name="del_book"),
    url(r'^add$', views.add_book, name="add_book"),
    url(r'^library$', views.library, name = "library")
]
