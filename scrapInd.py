import requests as re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time
import re

driver = webdriver.Chrome(executable_path="C:/Users/Schonanderl/Downloads/chromedriver_win32/chromedriver.exe")

url = "https://opencollective.com/airbnb#backer"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

data = []

for span in soup.find_all('span', {'class': 'Text__P-sc-18kcxxs-0-Clean-span bjQgdm'}):
    print(span.get_text())
    datapoint = {
        "Amount": span.get_text()
    }
    data.append(datapoint)

df = pd.DataFrame(data)

non_decimal = re.compile(r'[^\d]+')

df["Amount"] = df["Amount"].str.replace(non_decimal, "")

df["Amount"] = df["Amount"].astype('int32')

df.to_csv("AirBnBData.csv")