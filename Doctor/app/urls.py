from django.conf.urls import url
from app import views
from django.urls import path
#template urls!
app_name = 'app'

urlpatterns=[
    url(r'^about',views.about,name='about'),
    url(r'^blog',views.blog,name='blog'),
    url(r'^team',views.team,name='team'),
    url(r'^contact',views.contact,name='contact'),
    url(r'^clinics',views.clinics,name='clinics'),
    url(r'^appointment',views.appointment,name='appointment'),
    url(r'^appointment_success',views.appointment_success,name='appointment_success'),
]
