#import requests
import sys
import urllib2
from BeautifulSoup import BeautifulSoup

input_link = raw_input("Please enter the link below: ")

webpage = urllib2.urlopen(input_link)
#response = requests.get(webpage)
#html = response.content
print webpage
soup = BeautifulSoup(webpage)

for link in soup.findAll('a'):
    if(link.get('href').startswith("https://maps")):
        print 'These are the links which you\'ve asked for:'
        print link
