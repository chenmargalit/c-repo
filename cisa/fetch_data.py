import json
from bs4 import BeautifulSoup
import requests

from create_data_obj import CreateDataObj

class FectchData():
    
    def __init__(self, url):
        self.url = url
        self.textual_data = ''
        self.links = []
        self.data_to_return = []
    
    def get_data(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        for script in soup(['script', 'style']):
            script.extract()
        self.textual_data = soup
            
    def get_all_urls(self, num_of_advisories):
        counter = 1
        print(self.textual_data)
        div = self.textual_data.find('div', class_='item-list')
        ul = div.ul
        a_tags = ul.find_all('a')
        for link in a_tags:
            if counter <= num_of_advisories:
                self.links.append(link.attrs['href'].split('/')[3])
                counter+=1
    
    def get_data_from_all_links(self):
        c = CreateDataObj()
        for link in self.links:
            
            cve_id = c.get_cve_id(link)
            title = c.get_title()
            publication_date = c.get_publication_date()
            score = c.get_cvss_score()
            cvss_vecor = c.get_cvss_vector()
            reporter = c.get_reporter()
            for i in range(len(cve_id)):
                obj = {}
                obj['title'] = title
                obj['publication_date'] = publication_date
                obj['reporter'] = reporter
                obj['vector'] = cvss_vecor
                obj['id'] = cve_id[i]
                obj['score'] = score[i]
                self.data_to_return.append(json.dumps(obj))
        return self.data_to_return