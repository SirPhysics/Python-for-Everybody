import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location:')
print('Retrieving', url)

xml = urllib.request.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = ET.fromstring(xml)
counts = tree.findall('.//count')

counting = 0
summing = 0

for count in counts:
    counting += 1
    summing += int(count.text)
    
print('Count:', counting)
print('Sum:', summing)
