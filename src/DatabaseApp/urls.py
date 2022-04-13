from django.conf.urls import re_path, include
from DatabaseApp import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='home'),
    path('/',views.home, name='home'),
    path('updatedQuery', views.updatedQuery, name = 'updatedQuery'),
    path('protocolsQuery', views.protocolsQuery, name = 'protocolsQuery'),
    path('categoryQuery', views.categoryQuery, name = 'categoryQuery'),
    path('ratingQuery',views.ratingQuery, name='ratingQuery'),
    path('tagQuery', views.tagQuery, name='tagQuery'),
    path('keywordQuery', views.keywordQuery, name='keywordQuery'),
    path('updatedQueryMash',views.updatedQueryMash, name= 'updatedQueryMash'),
    path('usedAPIMash', views.usedAPIMash, name='usedAPIMash'),
    path('tagsMash', views.tagsMash, name='tagsMash'),
    path('keywordQueryMash', views.keywordQueryMash, name='keywordQueryMash')
]