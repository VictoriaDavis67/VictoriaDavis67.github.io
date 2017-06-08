#get all of the librares we need
from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request
#store the base_url
url = "https://github.com/humanitiesprogramming/scraping-corpus"
#using that url, get the HTML from it
html = request.urlopen(url).read()
#take the html we have a turn it into some soup we can work with
soup = BeautifulSoup(html, 'lxml')
#take that soup and find all of the anchor tags (links)
links = soup.find_all('a')[0:10]
#go through the soup and get all of the text (first 2000 characters)
text= soup.text[0:2000]
#for link in soup.select("td.content a"):
    #print(link.text)
#links_html = soup.select('td.content a')
#urls = []
#for link in links_html:
    #url = link['href']
    #urls.append(url)
#print(urls)
#go through the soup, grab all of the links that we care about (td tags with a content class that have a tag inside them)
links_html = soup.select('td.content a')
urls = []
#go through each url, get rid of 'blob/', and give me a link that adds the sub url to the base url. These will be useable links.
for link in links_html:
    url = link['href'].replace('blob/','')
    urls.append("https://raw.githubusercontent.com" + url)
#print(urls)
#creates an empty list called corpus texts
corpus_texts = []
#for each thing in urls, go through them
for url in urls:
    #print the url first
    #print(url)
    # open the url and getting the html at it
    html = request.urlopen(url).read()
    #convert the html we have into something we can use--a bunch of beautiful soup in this case

    soup = BeautifulSoup(html, "lxml")
    #get all of the text we have, then take all of the line breaks and replace them with
    text = soup.text.replace('\n', '')
    #take the text data and add it to the growing corpus
    corpus_texts.append(text)
# print out the contents of the thing
print(corpus_texts)
