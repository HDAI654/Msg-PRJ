from django.urls import path
from . import views
urlpatterns = [
    path('panel', views.main_page, name='main_page'),
    path('savemessage', views.savemessage, name='savemessage'),
    path('readmsg', views.readmsg, name='readmsg'),

]
