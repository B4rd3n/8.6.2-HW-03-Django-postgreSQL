from django.urls import path
from .views import author_upgrade

urlpatterns = [
    path('become_an_author/', author_upgrade, name = 'become_an_author')
]