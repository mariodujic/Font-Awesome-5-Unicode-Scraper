#! /usr/bin/env python3

import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://fontawesome.com/v5/cheatsheet'
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)

name_elements = browser.find_elements(By.CLASS_NAME, 'icon-name')
unicode_elements = browser.find_elements(By.CLASS_NAME, 'icon-unicode')

font_awesome_array = []

for name_element, unicode_element in zip(name_elements, unicode_elements):
    font_awesome_dict = dict(name=name_element.text, unicode=unicode_element.text)
    font_awesome_array.append(font_awesome_dict)

with open('font-awesome-unicodes.json', 'w') as outfile:
    json.dump(font_awesome_array, outfile)
