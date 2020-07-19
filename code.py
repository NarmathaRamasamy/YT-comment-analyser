from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
import time
url=input("ENTER THE URL: ")
driver.get(url)
time.sleep(5)
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     time.sleep(5)
     new_height = driver.execute_script("return document.body.scrollHeight")
     if new_height == last_height:
        break
     last_height = new_height      
comment1=driver.find_elements_by_xpath('//*[@id="contents"]')
l2=[]
for c in comment1:
    comments1=c.find_elements_by_xpath('//*[@id="content-text"]')
    for c1 in comments1:
        print(c1.text)
        l2.append(c1.text)
from textblob import TextBlob
positive=0.0
negative=0.0
neutral=0.0
polarity=0.0
def percentage(part,whole):
    res=part/whole
    return 100*res
for c in l2:
    analysis=TextBlob(c)
    polarity+=analysis.sentiment.polarity
    if(analysis.sentiment.polarity==0.0):
        neutral+=1
    if(analysis.sentiment.polarity>0.0):
        positive+=1
    if(analysis.sentiment.polarity<0.0):
        negative+=1  
print(positive,neutral,negative)
positive=percentage(positive,len(l2))
negative=percentage(negative,len(l2))
neutral=percentage(neutral,len(l2))
import matplotlib.pyplot as plt
positive=float(positive)
print("The result form comment section shows:")
labels=['positive ['+str(positive)+']%','neutral ['+str(neutral)+']%','negative ['+str(negative)+']%']
col=['yellow','blue','gray']
sizes=[positive,neutral,negative]
plt.pie(sizes,labels=labels,colors=col,startangle=90,shadow=True)
plt.title("COMMENT ANALYSIS")
plt.axis('equal')
plt.tight_layout()
