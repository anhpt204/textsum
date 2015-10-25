'''
Created on Oct 14, 2015

@author: pta
'''
from django.http.response import HttpResponse
from textsum.settings import NEWS_SUM_DIR
import glob
from news.models import NewsSum
from django.template import loader
from django.template.context import RequestContext
import os
from os.path import join

def show_news(request):
    
    dirs = os.listdir(NEWS_SUM_DIR)
    
    news_sums = []

    for dir in dirs:
        news = NewsSum(join(NEWS_SUM_DIR, dir))
        news_sums.append(news)
        
    template = loader.get_template('news_sum.html')
    context = RequestContext(request, {
        'news_sums': news_sums,
        })
    
    return HttpResponse(template.render(context))