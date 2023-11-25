import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

gecko_path = r'D:\Mastercourse Capstone Project 1\driver\geckodriver.exe'
service = Service(gecko_path)

options = Options()
options.headless = False  
driver = webdriver.Firefox(service=service, options=options)


csv_file_path = 'crypto.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    
    csv_writer = csv.writer(csv_file)

    header = ["Rank","SL NO", "Coin Name", "X","Price", "1h", "24h", "7d", "Y","24h Volume", "Market Cap"]
    csv_writer.writerow(header)

    
    for page_number in range(1, 101):
        
        driver.get(f"https://www.coingecko.com/?page={page_number}")

    
        driver.implicitly_wait(10)

        
        data_elements = driver.find_elements(By.CSS_SELECTOR, 'tbody.tw-divide-y tr')

       
        for row in data_elements:
            
            row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, 'td')]

            csv_writer.writerow(row_data)


driver.quit()
