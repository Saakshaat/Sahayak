from selenium import webdriver
import os
from talk import talk


def search_web(inp):
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in inp.lower():
        talk('Opening Youtube')
        indx = inp.lower().split().index('youtube')
        query = inp.split()[indx + 1:]
        driver.get("http://youtube.com/results?search_query=" + '+'.join(query))
        return

    if 'wikipedia' in inp.lower():
        talk('Opening Wikipedia')
        indx = inp.lower().split().index('wikipedia')
        query = inp.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
    if 'google' in inp.lower():
        indx = inp.lower().split().index('google')
        query = inp.split()[indx + 1:]
        driver.get("https://www.google.com/search?q=" + '+'.join(query))
    if 'search' in inp.lower():
        indx = inp.lower().split().index('search')
        query = inp.split()[indx + 1:]
        driver.get("https://www.google.com/search?q=" + '+'.join(query))
    else:
        driver.get("https://www.google.com/search?q=" + '+'.join(inp))
        print("https://www.google.com/search?q=" + '+'.join(inp))
