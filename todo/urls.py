from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /5
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),

    # ex: edit/5
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),

    # ex: delete/5
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete'),

    # ex: add
    url(r'^add', views.add, name='add'),

]