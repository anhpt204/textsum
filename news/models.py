# -*- encoding: utf-8 -*-

'''
Created on Oct 14, 2015

@author: pta
'''
from urlparse import urlsplit
from os.path import join
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField, BooleanField, URLField,\
    DateTimeField, FilePathField, DateField
from django.db.models.fields.related import ForeignKey
from textsum.settings import NEWS_SUM_DIR
from django.utils import timezone

class ImportLog(Model):
    date_import = DateField(verbose_name="Ngày import dữ liệu")
    dir_path = CharField(verbose_name="Thư mục dữ liệu",
                             max_length=50,
                             default=NEWS_SUM_DIR)

    
class TopicSum(Model):
    title=CharField(max_length=200)
    date_import = DateField(verbose_name='date imported')
    published = BooleanField(default=False)
    date_published=DateField(verbose_name='date published', null=True)
    
    def __unicode__(self):
        return u'%s' %(self.title)
    
#     def save(self, force_insert=False, force_update=False, using=None, 
#         update_fields=None):
#         if self.changed_data.contains(self.published):
#             if self.published:
#                 self.date_published = timezone.now()
#             else:
#                 self.date_published = None
#             
#             
#         return Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    def importFrom(self, path_dir):
        # for title
        title_file = join(path_dir, 'title')
        self.title=open(title_file).read() 
        self.published=False
        self.date_import = timezone.now()
        self.save()
        
        #for content
        content_file = join(path_dir, 'content')
        lines = open(content_file).readlines()
        print content_file
        print len(lines)
        n=len(lines)-1
        # load summary
#         self.summary={}
        for i in xrange(0,n, 2):
            newsSum = NewsSum()
            newsSum.in_topic = self
            newsSum.url = lines[i]
            newsSum.domain = urlsplit(lines[i]).netloc
            newsSum.summary = lines[i+1]
            newsSum.save()
            
        
class NewsSum(Model):
    
    url = URLField(verbose_name="URL")
    domain=CharField(verbose_name="Domain", max_length=50)
    summary = TextField(verbose_name="Tóm tắt")
    in_topic = ForeignKey(TopicSum, verbose_name="Thuộc chủ đề")
        
        
        
#     def __load(self, path_dir):
#         # for title
#         title_file = join(path_dir, 'title')
#         self.title=open(title_file).read() 
#         #for content
#         content_file = join(path_dir, 'content')
#         lines = open(content_file).readlines()
#         print content_file
#         print len(lines)
#         n=len(lines)-1
#         # load summary
#         self.summary={}
#         for i in xrange(0,n, 2):
#             k = lines[i]
#             
#             v = lines[i+1]
#             
#             if self.summary.has_key(k):
#                 self.summary[k].append(v)
#             else:
#                 domain=urlsplit(k).netloc
#                 self.summary[k] = [domain, v]
#             
            