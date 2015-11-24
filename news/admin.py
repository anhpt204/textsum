# -*- encoding: utf-8 -*-

'''
Created on Nov 15, 2015

@author: pta
'''
from django.contrib.admin.options import TabularInline, ModelAdmin
from news.models import NewsSum, TopicSum, ImportLog
from django.contrib import admin

class NewsSumInline(TabularInline):
    model = NewsSum
    fields = ('domain', 'summary')
    
class TopicSumAdmin(ModelAdmin):
    model = TopicSum
    fields = ('title', 'date_import', 'published')
    list_display=('title', 'date_import', 'published')
    list_filter=('date_import', 'published')
    actions = ['make_published']
    inlines=[NewsSumInline]
    
    def make_published(self, request, queryset):
        queryset.update(published=True)
    make_published.short_description = "Mark selected news as published"
    
class ImportLogAdmin(ModelAdmin):
    model=ImportLog
    
    list_display=('date_import', 'dir_path', 'importData')
    
    def importData(self, obj):
#         ds_dethi = obj.sinhDe()
#         print 'importing...'
        return u'<a href="%s">Import</a>' % ('/news/import/'+str(obj.pk)+'/')
    importData.allow_tags=True
    importData.short_description="Import"
    
    
admin.site.register(TopicSum, TopicSumAdmin)
admin.site.register(ImportLog, ImportLogAdmin)