import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

gecko_path = r'D:\Mastercourse Capstone Project 1\driver\geckodriver.exe'
service = Service(gecko_path)

options = Options()
options.headless = False  
driver = webdriver.Firefox(service=service, options=options)

csv_file_path = 'CryptocurrencyData.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    header = ["Rank","Coin Name", "Symbol", "Price", "1h", "24h", "7d","30d","24h Volume","Circulating Supply","Total Supply","Market Cap"]
    csv_writer.writerow(header)

    driver.get("https://www.coingecko.com/en/all-cryptocurrencies")
    driver.implicitly_wait(10)

    show_more_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[2]/div/a")

   
    while show_more_button.is_displayed():
        show_more_button.click()
        time.sleep(3)  

    
    data_table = driver.find_element(By.CLASS_NAME, 'table')

   
    rows = data_table.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
       
        cells = row.find_elements(By.TAG_NAME, 'td')

        
        row_data = [cell.text for cell in cells]
        csv_writer.writerow(row_data)

driver.quit()
