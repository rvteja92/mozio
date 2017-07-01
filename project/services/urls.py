'''Url Configuration for app'''

from django.conf.urls import url

from .views import (ListCreateProvidersView, RetrieveUpdateDeleteProviderView,
                    ListCreateServiceArea, RetrieveUpdateDeleteServiceAreaView)


urlpatterns = [
    url(r'^providers/all/', ListCreateProvidersView.as_view()),
    url(r'^providers/(?P<pk>[0-9a-f]+)/$', RetrieveUpdateDeleteProviderView.as_view()),
    url(r'^areas/all/$', ListCreateServiceArea.as_view()),
    url(r'^areas/(?P<pk>[0-9a-f]+)/$', RetrieveUpdateDeleteServiceAreaView.as_view()),
]
