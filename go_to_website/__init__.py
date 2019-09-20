from selenium import webdriver


def go_to_website(inp):
    import os
    query = ""
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
    if 'to' in inp.lower():
        indx = inp.lower().split().index('go to')
        query = inp.split()[indx + 1:]
    elif 'visit' in inp.lower():
        indx = inp.lower().split().index('visit')
        query = inp.split()[indx + 1:]
    driver.get("https://www." + query)
