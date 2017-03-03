import requests
import urllib
from BeautifulSoup import BeautifulSoup

url = 'http://rockefeller100.org/'
response = requests.get(url)
html = response.content
#print html

soup = BeautifulSoup(html)
count = 0
image_links = [image.get('src') for image in soup.findAll('img')]
        # print image.get('src')
        # count=count+1
print image_links
print len(image_links)
#print count, "images are found"

out = open('links.txt', 'w')
print out
[out.write(i+'\n') for i in image_links]
out.close()
input_txt = open('links.txt', 'r')
for link in input_txt:
        print link
        url = link
        image = link.rsplit('/', 1)[1]
        urllib.urlretrieve(url, image)
input_txt.close()