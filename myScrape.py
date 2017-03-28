import requests
import urllib
import string
from BeautifulSoup import BeautifulSoup

url = 'http://rockefeller100.org/exhibits/show/agriculture'
response = requests.get(url)
html = response.content
#print html

soup = BeautifulSoup(html)
count = 0
image_links = [image.get('src') for image in soup.findAll('img')]
        # print image.get('src')
        # count=count+1
#print image_links
print "%d image links are found" %(len(image_links))
#print count, "images are found"

out = open('links.txt', 'w')
print out
[out.write(i+'\n') for i in image_links]
out.close()
input_txt = open('links.txt', 'r')
for link in input_txt:
        #image = url.rsplit('/', 1)[1]
        #urllib.urlretrieve(url, 'static/images'+image)
        filename = link.rsplit('/')[-1]
        print filename
        if 'jpg' in link:
                print 'image found'
                try:
                        urllib.urlretrieve(link, 'static/images/'+filename)
                except IOError:
                        print 'yeah'
        else:
                print 'not found'
        
input_txt.close()