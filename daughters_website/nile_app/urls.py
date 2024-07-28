from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('community/', views.community, name='community'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('post/', views.post, name='post'),
    path('programs/', views.programs, name='programs'),
    path('resources/', views.resources, name='resources'),
    path('signup/', views.signup, name='signup'),
]
