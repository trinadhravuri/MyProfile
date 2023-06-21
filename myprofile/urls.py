from django.urls import path
from . import views
urlpatterns= [
    path('',views.home,name='home'),
    path('base',views.base),
    path('allskills',views.allskills,name='allskills'),
    path('allprojects',views.allprojects,name='allprojects'),
]