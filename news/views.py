# -*- encoding: utf-8 -*-

'''
Created on Oct 14, 2015

@author: pta
'''
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.http.response import HttpResponse
from textsum.settings import NEWS_SUM_DIR
import glob
from news.models import NewsSum, ImportLog, TopicSum
from django.template import loader
from django.template.context import RequestContext
import os
from os.path import join
from django.utils import timezone


def import_data(request, pk):
    importLog = ImportLog.objects.get(pk=pk)
    
    dirs = os.listdir(importLog.dir_path)

    for dir in dirs:
        dir_path = join(importLog.dir_path, dir)
        topicSum = TopicSum()
        topicSum.importFrom(dir_path)
    return HttpResponse("Import Complete")
    
class Topic:
    def __init__(self, topicSum):
        self.title = topicSum.title
        self.summary = {}
        for news in topicSum.newssum_set.all():
            if not self.summary.has_key(news.domain):
                self.summary[news.domain] = [news.url, news.summary]
            else:
                self.summary[news.domain].append(news.summary)
                
        
def show_news(request):
    
    topics = TopicSum.objects.filter(published=True)
            
#     print len(topics)
    news_sums = []
    for topic in topics:
        news_sums.append(Topic(topic))
        
    template = loader.get_template('news_sum.html')
    context = RequestContext(request, {
        'news_sums': news_sums,
        })
    
    return HttpResponse(template.render(context))

def to_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
#     pdfmetrics.registerEncoding('utf-8')
    textObj = p.beginText()
    textObj.setTextOrigin(inch, 10*inch)
    
    textObj.setFont("Arial", 12)
    
    topics = TopicSum.objects.filter(published=True)
    for topic in topics:
        textObj.textLine(topic.title)
#     textObj.textOut(u"Giá vàng trong nước hôm nay theo đà ngày hôm qua , tiếp tục thiết lập mốc giá mới chạm ngưỡng 34,15 triệu đồng/lượng , đánh dấu mức cao nhất kể từ ngày 26.9 .")
    
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
#     p.drawString(-inch, -inch, "Hello world.")
    p.drawText(textObj)
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
#     return HttpResponse('export to pdf')