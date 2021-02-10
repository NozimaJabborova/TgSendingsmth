import requests 
import json
from pprint import pprint
#token='1656085440:AAFwae2Sy-ABI0JtrToivLMI1QiB7WoNCys'
token='1656085440:AAFz1LuUJC6hL4tk_NVC8shyw0ArnQ1ET9g'
url=f'https://api.telegram.org/bot{token}/getUpdates'
r=requests.get(url)
#print(r.url)
data=r.json()
#user=r.json()
updates=data['results']
pprint(len(updates))