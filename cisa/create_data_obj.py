from bs4 import BeautifulSoup
import requests
import re

class CreateDataObj():
    
    def get_data(self, link):
        page = requests.get(f'https://www.cisa.gov/uscert/ics/advisories/{link}')
        soup = BeautifulSoup(page.content, "html.parser")
        for script in soup(['script', 'style']):
            script.extract()
        self.data = soup
    
    def get_cve_id(self, link):
        self.get_data(link)
        cve_arr = []
        for ptag in self.data.find_all('p'):
            p = ptag.text
            res = re.findall('CVE-\d+\-\d+', p)
            if len(res) > 0:
                cve_arr.append(res)
        return cve_arr

    def get_title(self):
        return self.data.find('title').string
    
    def get_publication_date(self):
        return self.data.find('div', class_='submitted meta-text').text.split('date:')[1].strip()
    
    def get_cvss_score(self):
        scores = []
#         res = re.findall("score of \d+\.\d", self.data.text)[0].split('of ')[1] 
        res = self.data.find_all(lambda tag:tag.name=="p" and "score of" in tag.text)
        for score in res:
            scores.append(score.text.split('score of')[1].split('has')[0].strip())
        return scores
        
    
    def get_cvss_vector(self):
        res = self.data.find(lambda tag:tag.name=="p" and "vector string is" in tag.text)
        if res:
            return res.text.split('vector string is')[1]
        else:
            return None
        
    def get_reporter(self):
        res = self.data.find(lambda tag:tag.name=="p" and "reported" in tag.text)
        if res:
            return res.text.split('reported')[0]
        else:
            return None