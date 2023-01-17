import random
import time

import pandas as pd
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

opts = Options()
url = "https://www.linkedin.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# function to ensure all key data fields have avalue
def validate_field(field):
    if field:
        pass
    else:
        field = 'No results'
    return field


driver.get(url)
username = driver.find_elements()
password = driver.find_elements()
signIn = driver.find_elements()
sleep(15)

for x in range(0, 20, 10):
    driver.get(url)
    time.sleep(random.uniform(2.5, 4.9))

