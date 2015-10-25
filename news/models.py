'''
Created on Oct 14, 2015

@author: pta
'''
from urlparse import urlsplit
from os.path import join

class NewsSum:
    def __init__(self, path_dir):
        self.title=''
        self.img=None
                
        self.__load(path_dir)
        
        
    def __load(self, path_dir):
        # for title
        title_file = join(path_dir, 'title')
        self.title=open(title_file).read() 
        #for content
        content_file = join(path_dir, 'content')
        lines = open(content_file).readlines()
        print content_file
        print len(lines)
        n=len(lines)-1
        # load summary
        self.summary={}
        for i in xrange(0,n, 2):
            k = lines[i]
            
            v = lines[i+1]
            
            if self.summary.has_key(k):
                self.summary[k].append(v)
            else:
                domain=urlsplit(k).netloc
                self.summary[k] = [domain, v]
            
            