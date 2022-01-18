import re
import requests

from scrapper import Scrapper

class GetAllData:
    
    def __init__(self, urls):
        self.urls = urls
        self.all_data = []
        self.url_data = ''
        
    def fetch_urls(self):
        s = Scrapper()
        # currently blocked and not able to get any more data and finish this.
        ids_list = s.get_ids()
        
        
    def fetch_url_data(self, url):
        self.url_data = requests.get(url).text
        
        
    def return_func_data(self, func):
        arr = []
        res = func()
        for item in res:
            arr.append(item.strip())
        return arr
        
    def get_ids(self):
        ids = re.findall('CVE-\d+\-\d+', self.url_data)
        return ids
    
    def get_scores(self):
        scores = re.findall('Base Score:(.*)', self.url_data)
        scores.pop(0)
        return scores
    
    def get_vectors(self):
        vectors = re.findall('CVSS:\d+\.\d+\/(.*)', self.url_data)
        return vectors
    
    def get_title(self):
        title = re.findall('SSA-\d+:(.*)', self.url_data)
        return title

    def get_publication_date(self):
        publication_date = re.findall('Publication Date:(.*)', self.url_data)[0].strip()
        return publication_date
        
    def generate_all_data(self):
        for url in self.urls:
            self.fetch_url_data(url)
            objs = []
            ids = self.get_ids()
            for i in range(len(ids)):
                obj = {}
                obj['id'] = ids[i]
                obj['score'] = self.return_func_data(self.get_scores)[i]
                obj['vector'] = self.return_func_data(self.get_vectors)[i]  
                obj['publication_date'] = self.get_publication_date()
                obj['title'] = (self.return_func_data(self.get_title)[0])
                objs.append(obj)
                self.all_data.append(obj)
        return self.all_data