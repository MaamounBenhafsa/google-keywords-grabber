import random
import requests
import string
import xml.etree.ElementTree as ET
from googlesearch import search
import datetime
date=datetime.datetime.now()
lst = [] 
name= random.randint(1,9999)
output=str(name)
to_output = open(output,'x')
print("""
  _  __                                _        _____           _     _               
 | |/ /                               | |      / ____|         | |   | |              
 | ' / ___ _   ___      _____  _ __ __| |___  | |  __ _ __ __ _| |__ | |__   ___ _ __ 
 |  < / _ \ | | \ \ /\ / / _ \| '__/ _` / __| | | |_ | '__/ _` | '_ \| '_ \ / _ \ '__|
 | . \  __/ |_| |\ V  V / (_) | | | (_| \__ \ | |__| | | | (_| | |_) | |_) |  __/ |   
 |_|\_\___|\__, | \_/\_/ \___/|_|  \__,_|___/  \_____|_|  \__,_|_.__/|_.__/ \___|_|   
            __/ |                                                                     
           |___/                                                                      
           {} 
           {}

           """.format(date,"by mamoun benhafsa"))

n = int(input("Put Number Of Keywords you will search >> ")) 
  
for i in range(0, n): 
    ele = str(input()) 
  
    lst.append(ele) 
      

print("Getting Keywords For {} To {} File".format(lst,name))
print("Trap CTRL-C To Stop The Script")



list_b = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "z","ü", "ä", "ö", "y", "w", "x"] 
list_c = [f"{i} {j}" for i in lst for j in list_b]
               
for x in list_c:
    apiurl = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=de&q=" + x
    r = requests.get(apiurl)
    tree = ET.fromstring(r.text)
    for child in tree.iter('suggestion'):
        dta=child.attrib['data']
        print(dta)
        to_output.write(dta+'\n')

    
