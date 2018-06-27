from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.helloworld, name='helloworld'),
    url(r'^testpage/', views.index_template, name='index_template'),
    url(r'^form$', views.form_test),
]
