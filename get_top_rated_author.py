import requests 
from bs4 import BeautifulSoup 
import time
import codecs



Author=[]
UserPoints=[]
Title=[]
comments=[]
listOfTitles=[]
ListOfSubtext=[]
ListOfComments=[]
AuthorDetails=[]

URL = "https://news.ycombinator.com/news"
r=requests.get(URL)

#page Number is the variable here you can mention the unique number for how many 
#pages you want to scrap the data
pageNumber=25
soup = BeautifulSoup(r.content, 'html.parser') 
for page in range(1,pageNumber+1):
     URL = "https://news.ycombinator.com/news?p="+str(page)
     r=requests.get(URL)
     soup = BeautifulSoup(r.content, 'html.parser') 
     listOfTitles.append(soup.find_all('td',attrs = {'class':'title'}))
     ListOfSubtext.append(soup.find_all('td',attrs={'class':'subtext'})) 
     ListOfComments.append(soup.find_all('a')) 
     


        


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
   for cmt in cmt1:
      if cmt.text.encode('utf-8').__contains__('comments') and cmt.text.encode('ascii', 'ignore')[0].isdigit():
        comments.append(cmt.text.encode('ascii', 'ignore'))   
      if cmt.text.encode('ascii', 'ignore').__contains__('discuss') :    
        comments.append('0 comments')
    
   #print 'comments',comments   
for title1 in listOfTitles:
   for title in title1:   
      if title.text.encode('ASCII','ignore')=='More':
       continue
      Title.append(title.text.encode('ASCII','ignore'))




#print "Length of list of Title is ",len(listOfTitles)    
for data in Title: 
    if data[0].isdigit():
        Title.remove(data) 



for i in range(0,len(Author)):
  AuthorDetails.append([Author[i],UserPoints[i]])   
 
for data in AuthorDetails:
    print "User Name :",data[0]," \n\t Karma Points :",data[1],"\n\n"



#print "Length of Author  is ",len(Author)
#print "Length of UserPoints  is ",len(UserPoints)
   
    
