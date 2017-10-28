from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^createCard/$',views.createCard,name = 'Create Card'),
    url(r'^confirm/$',views.confirm,name = 'confirm'),
    url(r'^cards/$',views.cards,name = 'cards'),
    url(r'^register/$',views.register,name = 'register'),
    url(r'^login/$',views.userlogin,name = 'login'),
    url(r'^logout/$',views.userlogout,name = 'logout'),
]