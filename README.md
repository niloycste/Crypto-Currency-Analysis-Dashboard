# Crypto-Currency-Analysis-Dashboard
## Problem Statement: Cryptocurrency Market Analysis
The objective of this Crypto analysis is to gain valuable insights into the cryptocurrency market from this website: https://www.coingecko.com/en/all-cryptocurrencies. 
Later we utilized the scraped data to understand the following Trends and relations using Tableau Dashboard:

1. Performance Trends: Visualize and compare the performance trends (1h, 24h, 7d, 30d) of different cryptocurrencies based on their respective Coin Names.
2. Market Metrics Overview: Create comprehensive visualizations comparing Top Coin Names against essential metrics, including Price, 24-hour Volume, Circulating Supply, and Market Cap.
3. Aggregate Metrics: Calculate and visualize aggregate metrics such as Total Market Cap, Total 24-hour Volume, and Total Circulating Supply across all cryptocurrencies.
You can visit the public dashboard from here: https://public.tableau.com/app/profile/niloy/viz/Crypto-CurrencyAnalysisDashboard/OverallAnalysisOfCrypto

## Build From Sources & Selenium Scraper 
1. Clone the repo
```bash
git clone https://github.com/niloycste/Crypto-Currency-Analysis-Dashboard.git
```
2. Initialize and Activate Virtual Environment
```bash
virtualenv env
source env/Scripts/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Download the Firefox web driver
```bash
https://github.com/mozilla/geckodriver/releases
```
5. Run the Scrapper
```bash
python coingeckoupdated.py
```
6. anyone can get a file name "CryptocurrencyData.csv" containing all the desired columns
## Analytics 
Tableau Public View: https://public.tableau.com/app/profile/niloy/viz/Crypto-CurrencyAnalysisDashboard/OverallAnalysisOfCrypto
