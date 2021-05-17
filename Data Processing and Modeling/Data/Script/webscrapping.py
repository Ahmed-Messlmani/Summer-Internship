from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome(executable_path=r'D:/chromedriver/chromedriver.exe')
titles=[] #List to store name of the product
categories=[] #List to store price of the product
hashtags=[] #List to store rating of the product
driver.get("https://www.kaggle.com/ljlr34449/porn-data")
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
for a in soup.find_all('div',attrs={'class':'sc-pAqos sc-jIDfPw fkWPpT'}):
	title=a.findAll('div')[5]
	categorie=a.findAll('div')[8]
	hashtag=a.findAll('div')[9]
	titles.append(title.text)
	categories.append(categorie.text) 
	hashtags.append(hashtag.text)
df = pd.DataFrame({'titles':titles,'categories':categories,'hashtags':hashtags}) 
df.to_csv('data.csv', index=False, encoding='utf-8')