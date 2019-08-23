from selenium import webdriver
import os
from talk import talk


def youtube(inp):
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
    talk('Opening Youtube')
    indx = inp.lower().split().index('youtube')
    query = inp.split()[indx + 1:]
    driver.get("http://youtube.com/results?search_query=" + '+'.join(query))
    return
