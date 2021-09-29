Task:
Answer the question: how long is a user registered on GitHub
------------------------------------

import requests
import os
from pprint import pprint
import dateutil.parser, datetime

#generate tocken on GitHub
owner = input("Print user's login: ")
access_token='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' 
headers = {'Authorization':"Token "+access_token}

#parse url
url=f"https://api.github.com/users/{owner}" 
info=requests.get(url,headers=headers).json()

#get current date and registration dates
current_date = datetime.datetime.now() 
registration_date = dateutil.parser.parse(info['created_at'], ignoretz=True)

#how many days is a user registered?
pprint((current_date - registration_date).days) 

