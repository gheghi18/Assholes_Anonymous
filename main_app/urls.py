from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^createCard/$',views.createCard,name = 'Create Card'),
    url(r'^confirm/$',views.confirm,name = 'confirm')
]