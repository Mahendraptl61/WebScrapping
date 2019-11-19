import requests 
from bs4 import BeautifulSoup 
import time
import codecs
import re
def Sort(sub_li): 
    return(sorted(sub_li, key = lambda x: x[1])) 

Author=[]
UserPoints=[]
Title=[]
comments=[]
listOfTitles=[]
ListOfSubtext=[]
ListOfComments=[]
CommentAndStory=[]
URL = "https://news.ycombinator.com/news"
r=requests.get(URL)
pageNumber=30
soup = BeautifulSoup(r.content, 'html.parser') 
for page in range(1,2):
     URL = "https://news.ycombinator.com/news?p="+str(page)
     r=requests.get(URL)
     soup = BeautifulSoup(r.content, 'html.parser') 
     listOfTitles.append(soup.find_all('td',attrs = {'class':'title'}))
     ListOfSubtext.append(soup.find_all('td',attrs={'class':'subtext'})) 
     ListOfComments.append(soup.find_all('a',href=True)) 
     


        


for User in ListOfSubtext:
   for  user in User:  
      if isinstance(user,unicode): 
          continue
      sp1=BeautifulSoup(str(user),'html.parser')
      usr1=sp1.find('span',attrs={'class':'score'})
      if usr1==None:
          continue
      UserPoints.append(usr1.text)
      author=sp1.find('a',{'class':'hnuser'})
      Author.append(author.text)
    

for cmt1 in ListOfComments:
   count=0 
   for cmt in cmt1:
      if cmt.text.encode('utf-8').__contains__('comments') and cmt.text.encode('utf-8')[0].isdigit():
        count+=1
        print 
        comments.append(cmt.text.encode('utf-8'))   
      if cmt.text.encode('utf-8').__contains__('discuss') :    
        count+=1
        print 
        comments.append('0 comments')
 
   count=0 
for title1 in listOfTitles:
   for title in title1:   
      if title.text.encode('utf-8')=='More':
       continue
      Title.append(title.text.encode('utf-8'))





    
for data in Title: 
    if data[0].isdigit():
        Title.remove(data) 



for i in range(0,len(comments)):
     dt1=''
     for cmt in comments[i]:
         if cmt.isdigit():
           dt1=dt1+cmt     
     CommentAndStory.append([Title[i],int(dt1)])
     dt1=''




for data in Sort(CommentAndStory):
    print "\n\n",data[0]," ",data[1]," Comments Given By The User ",



#print "\n\ncomments  and length is ",len(comments)
#print "\n\ntitle and length is ",len(Title)



