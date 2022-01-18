import re


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class Scrapper():
    
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get('https://new.siemens.com/global/en/products/services/cert.html#SecurityPublications')
    
    def get_ids(self):
        try:   
            res = self.driver.find_elements(By.TAG_NAME, 'tr')
            ids = []
            for index, item in enumerate(res):
                id = re.findall('SSA-\d+', item.text)
                if len(id) > 0:
                    ids.append(id[0].split('-')[1])
            return ids
        except Exception as e:
            print('failed to fetch ids')
            return e
        
        finally:
            self.driver.quit()