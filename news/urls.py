'''
Created on Oct 14, 2015

@author: pta
'''

import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.show_news, name='show_news'),
#     url(r'^login/$', views.login_user, name='login_user'),
        
]