'''
Created on Oct 14, 2015

@author: pta
'''

import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.show_news, name='show_news'),
    url(r'^import/(?P<pk>[\d]+)/$', views.import_data, name='import_data'),
    url(r'^to-pdf/$', views.to_pdf, name='to_pdf'),
    
    
#     url(r'^login/$', views.login_user, name='login_user'),
        
]