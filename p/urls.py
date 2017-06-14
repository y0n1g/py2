from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/(?P<op>\w+)/(?P<var>\w+)$', views.test, name='test'),
]
