from django.urls import path
from . import views
urlpatterns= [
    path('',views.home,name='home'),
    path('allskills',views.my_skills,name='allskills'),
]