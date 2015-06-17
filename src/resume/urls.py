from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.PositionListView.as_view(), name='position-list'),
    url(r'^$', views.positions_list, name='position-list'),
    url(r'^position/$', views.PositionCreateView.as_view(), name='position_add'),
    url(r'^position/(?P<pk>[0-9]+)/$', views.PositionUpdateView.as_view(), name='position_update'),
    url(r'^position/(?P<pk>[0-9]+)/delete/$', views.PositionDeleteView.as_view(), name='position_delete'),
]
