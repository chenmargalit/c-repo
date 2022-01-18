from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
import re
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# driver = webdriver.Chrome(ChromeDriverManager().install())
# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--headless')
# options.add_argument("--window-size=1920,1080")

# driver = webdriver.Firefox()
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://new.siemens.com/global/en/products/services/cert.html#SecurityPublications')


res = driver.find_elements(By.TAG_NAME, 'tr')
ids = []
for index, item in enumerate(res):
    id = re.findall('SSA-\d+', item.text)
    if len(id) > 0:
        # print(id[0].split('-')[1])
        ids.append(id[0].split('-')[1])
print(ids)


        



        # def print_ids(num_of_results_wanted):
#     ids_arr = []
#     res = driver.find_elements(By.TAG_NAME, 'td')
#     print(res)
#     # for _, item in enumerate(res):
#     #     ids = re.findall('SSA-\d+', item.text)
#     #     for i in range(num_of_results_wanted):
#     #         print(i)
#     #         print(ids)
#     # return ids_arr


# def get_ids(num_of_ids):

#     rounds_number = math.ceil(num_of_ids / 15)
#     num_ids_returned = 0

#     try:
#         # element = WebDriverWait(driver, 20).until(
#         #     EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
#         # )
#         # # a =  driver.find_element(By.ID, 'onetrust-accept-btn-handler')
#         # element.click()
#         WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"onetrust-accept-btn-handler"))).click()

#         l=driver.find_element(By.XPATH, "//a[@title='Next']")
#         ids = print_ids(num_of_ids)
#         print('ids are', ids)
#         # for i in range(rounds_number):
#         #     l.click()
#         #     ids = print_ids(num_of_ids)
#         #     num_ids_returned = len(ids)


#         WebDriverWait(driver, 10)
#         # driver.implicitly_wait(10)


#     finally:
#         print('number of ids', num_ids_returned)
#         driver.quit()
#         pass