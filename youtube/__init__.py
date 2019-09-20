from selenium import webdriver
import os
from talk import talk


def youtube(inp):
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
    if 'youtube' in inp:
        indx = inp.lower().split().index('youtube')
        query = inp.split()[indx + 1:]
        driver.get("https://www.youtube.com/results?search_query=" + '+'.join(query))
        return
    elif 'play' in inp:
        indx = inp.lower().split().index('play')
        query = inp.split()[indx + 1:]
        driver.get("https://www.youtube.com/results?search_query=" + '+'.join(query))
        return
    talk('Opening Youtube')
