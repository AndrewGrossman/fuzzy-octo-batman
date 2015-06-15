from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ResumePage.as_view(), name='main'),
]
