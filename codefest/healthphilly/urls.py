from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^search', views.SearchView.as_view(), name='search'),
    url(r'^map', views.map, name='map'),
]
