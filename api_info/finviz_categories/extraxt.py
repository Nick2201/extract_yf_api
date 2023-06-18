from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep
from pathlib import Path
from bs4 import BeautifulSoup
import json


from bs4 import BeautifulSoup
import os
import json
import re

docs = (Path(Path.cwd()/'api_info'/"docs"))
finviz = Path(docs/"finviz_filters.json")



def driver_func(headless: bool = True):
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', True)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference('browser.helperApps.neverAsk.saveToDisk',
                           'text/plain, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    if headless:
        options.add_argument('-headless')  # True - скрывает отображение работы браузера
    service = Service(r"\geckodriver.exe")
    return webdriver.Firefox(service=service, options=options)
links =[
    "https://finviz.com/screener.ashx?v=111"
    "https://finviz.com/screener.ashx?v=111&ft=2"
    "https://finviz.com/screener.ashx?v=111&ft=3"]

def get_page(link):
    _driver = driver_func()
    _driver.get(link)

    # _list = _driver.find_elements(By.CLASS_NAME,value="screener-combo-text")
    # [print(i.text) for i in _list]
    page = _driver.page_source
    _driver.close()
    _driver.quit()
    return page






def parse_finviz(html_doc):
    global key_name
    soup = BeautifulSoup(file, "html.parser")

    screener_basic_table = soup.findAll('tbody')[10]

    every_rows = screener_basic_table.findAll('td')
    dict_measure = {}
    for row in every_rows:

        if row.span is not None:
            key_name = (row.get_text()).replace('\n', '')
            hide_text = row.find('span',class_="screener-combo-title").get('data-boxover')



            extract_text = re.findall("class='tooltip_tab'>(.*?)</td>", hide_text)[0]
            # print(extract_text)
        else:
            if key_name in dict_measure:
                pass
            else:
                options_catalogue = (row.findAll('option'))

                dict_measure[key_name] = {'values':[option.text for option in options_catalogue],'explainer':extract_text}

    return dict_measure

def make_json_file(path_name,info):
    with open(path_name,'w') as file:
        json.dump(info,file)

FILE_PATH = r"D:\5. Nick\Code\finviz_filters.json"
if __name__ == '__main__':
    url = r"D:\5. Nick\Code\Stock Screener - Overview.html"
    
    with open (url,"r") as file:
        [get_list(link) for link in links]
        

        need_dict = parse_finviz(file)

        # path_name = r"D:\5. Nick\Code"
        # new_path = os.path.join(path_name,'finviz_filters.json')
        make_json_file(finviz,need_dict) # create json



