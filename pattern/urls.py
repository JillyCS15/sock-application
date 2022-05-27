from django.urls import path

from . import views

app_name = 'pattern'

urlpatterns = [
    path('home', views.pattern_page, name='pattern'),
    path('delete', views.delete_shacl, name="delete"),
]
