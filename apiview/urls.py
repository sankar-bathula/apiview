"""apiview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls import url,include
from apiviewapp import views
from rest_framework import routers
from rest_framework.authtoken import views as views1
router = routers.DefaultRouter()
router.register(r'test-viewset', views.TestViewSets, basename='test-viewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.TestAPIView.as_view()),
    #path('', views.EmployeeListView.as_view()),
    #path('api/' , views.EmployeeAPIView.as_view()),
    #path('api/' , views.EmployeeCreateAPIView.as_view()),
    #re_path('^api/(?P<id>\d+)/$' , views.EmployeeRetrieveAPIView.as_view()),
    #re_path('^api/(?P<id>\d+)/$', views.EmployeeUpdateAPIView.as_view()),
    #re_path('^api/(?P<id>\d+)/$', views.EmployeeDeleteAPIView.as_view()),
    #re_path('api', views.EmployeeListCreateAPIView.as_view()),
    #re_path('^api/(?P<id>\d+)/$', views.EmployeeRetrieveUpdateAPIView.as_view()),
    #re_path('^api/(?P<id>\d+)/$', views.EmployeeRetrieveDestroyAPIView.as_view()),
    #re_path('^api/(?P<id>\d+)/$', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    #re_path('^api_mixins/(?P<pk>\d+)/$', views.EmployeeDetailsViewMixins.as_view()),
    re_path('api_mixins/', views.EmployeeListModelMixins.as_view()),
    re_path('api-token-auth/', views1.obtain_auth_token, name='api-token-auth'),

    #path('', include(router.urls)),
]
