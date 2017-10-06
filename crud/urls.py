from django.conf.urls import url
#from django.contrib import admin

from .views import index
from .views import editar

urlpatterns = [
    url(r'^$', index, name= 'crudindex'), # expresion regular
    url(r'^editar/(?P<pk>[0-9]+)$', editar, name= 'crudeditar'),
]
