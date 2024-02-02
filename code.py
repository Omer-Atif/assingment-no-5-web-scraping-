from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://islamqa.info/en/categories/very-important/120/answers/46505/islam-erases-the-sins-that-came-before-it"
response=requests.get(url)
soup=BeautifulSoup(response.content,"html5")

title=soup.find(class_="title is-4 is-size-5-touch")
#print(title.text)

question=soup.find(class_="single_fatwa__question text-justified")
#print(question.text)

answer=soup.find(class_="single_fatwa__answer")
#print(answer.text)

data=[[title,question,answer]]
df=pd.DataFrame(data,columns=["title","question","answer"])
print(df)
df.to_csv("Assignment #05(web scraping) .csv")
print("work done")

