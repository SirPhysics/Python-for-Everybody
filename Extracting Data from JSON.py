import urllib.request as ur
import json

url = input('Enter location:')
#"http://py4e-data.dr-chuck.net/comments_1394117.json"
print('Retrieving:',url)
data = ur.urlopen(url).read()
print('Received:',len(data),"characters")

counting = 0
sum = 0
data_load = json.loads(data)
for item in data_load['comments']:
    counting += 1
    sum += int(item['count'])
print('Count: ',counting)
print('Sum:',sum)
