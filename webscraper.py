
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


content=[]
ans={}
a=[7811611,8012515,7976828,7867948,8202545,8202906,8329230,8618050,8513456,8802163]
start=1
    
for i in a:
    for j in range(1,10):
        url="http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r="+str(j)+"&f=G&l=50&co1=AND&d=PTXT&s1="+str(i)+"&OS="+str(i)+"&RS="+str(i)
        try:
            r=requests.get(url,headers = {
         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'},verify=False)
        except(requests.ConnectTimeout,requests.HTTPError,requests.ReadTimeout):   
            print("Error")
        
        data=BeautifulSoup(r.text,'html.parser')
        row1=data.find_all("table")[2]
        row1=row1.find_all("td")
        if int(row1[1].text.replace(',',''))==i:
                ans['pid']=row1[1].text.replace(',','')
                ans['title']=data.find_all("font")[3].text
                ans['abstract']=data.find("p").text
                ans['inventor']=data.find_all("table")[3].td.text
                
                #for f in data.find_all("table")[3].findChildren("tr"):
                #       if f.th.text.replace('\n','').replace(" ","")=="Inventors:":
                #          inventor=f.td.text.replace('\n','')
                #         break
                #    else:
                #       inventor=''
                #ans['inventor']=inventor
                l=data.find_all("table")[3].findNextSiblings("tr")
                for f in l:
                        if f.th.text.replace('\n','').replace(" ","")=="Filed:":
                            filed=f.td.text.replace('\n','')
                            break
                        else:
                            filed=''
                ans['Filed']=filed
                m=data.find_all("table")[3].findNextSiblings("tr")
                for asi in m:
                        if asi.th.text.replace('\n','').replace(" ","")=="Assignee:":
                            assignee=asi.td.text.replace('\n','')
                            break
                        else:
                            assignee=''
                ans['Assignee']=assignee
                print("Patent No: "+ans['pid']+'\n'+"Title: "+ans['title']+'\n'+"Abstract: "+ans['abstract']+'\n'+"Inventor: "+ans['inventor']+'\n'+"Filed: "+ans['Filed']+'\n'+"Assignee: "+ans['Assignee']+"\n\n")
                break
        else:
                continue
                
        
        
         
         

