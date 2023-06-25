"""
# Extract feed details from RSS in Python
RSS = Rich Site Summary

RSS means Rich Site Summary and uses standard web formats to publish information that changes frequently like blog posts, news, audio, video, etc. RSS documents often know as feed which consists of text, and metadata, like time and author’s name.

# Getting RSS feed

Use the feedparser.parse() function for creating a feed object which contains parsed blog. It takes the URL of the blog feed.
"""

#importing the modules
import feedparser

# fetch the feed with the url
feed_url = 'https://vaibhavkumar.hashnode.dev/rss.xml'

blog_feed = feedparser.parse(feed_url)

#importing the modules
import feedparser

# fetch the feed with the URL
feed_url = 'https://vaibhavkumar.hashnode.dev/rss.xml'

blog_feed = feedparser.parse(feed_url)

# returns link and number of blogs (entries) in the site
blog_link = blog_feed.feed.link
num_entries = len(blog_feed.entries)

# details of individual blog accessed by the attribute name
print(blog_feed.entries[0].title)
print(blog_feed.entries[0].link)
print(blog_feed.entries[0].author)
print(blog_feed.entries[0].published)

# getting list of tags and authors
tags = []
authors = []

if hasattr(blog_feed.entries[0], 'tags'):
    tags = [tag.term for tag in blog_feed.entries[0].tags]
if hasattr(blog_feed.entries[0], 'authors'):
    authors = [author.name for author in blog_feed.entries[0].authors]

print(tags)
print(authors)


"""
Now use the above code to write a function that takes the link of RSS feed and returns the details.
"""

def Rss_feed(rss=None):
    #taking the link of the RSS feed
    if rss is not None:
        import feedparser
        #parsing the blog feed
        blog_feed = blog_feed = feedparser.parse(rss)

        #getting list of the blog entries
        entries = blog_feed.entries

        #holding the details in the dictionary form
        details = {"Blog title":blog_feed.feed.title,
                   "Blog link":blog_feed.feed.link}
        
        #making a list for the iteration
        p_list=[]

        #iterating over each one of the details
        for entry in entries:
            temp=dict()

            #using try and except statement to avoid the error during the execution
            try:
                temp["title"]=entry.title
                temp["link"]=entry.link
                temp["author"]=entry.author
                temp["published"]=entry.published
                temp["authors"]=[author.name for author in entry.author]
                temp["summary"]=entry.summary
            except:
                pass
            p_list.append(temp)

        details["entries"]=p_list
        return details
    else:
        return None

if __name__=="__main__":
    import json
    feed_url="https://vaibhavkumar.hashnode.dev/rss.xml"
    datas = Rss_feed(rss=feed_url)

    if datas:
        print(json.dumps(datas,indent=2))
    else:
        print("None")




"""
Name property is provided by Beautiful Soup which is a web scraping framework for Python. Web scraping is the process of extracting data from the website using automated tools to make the process faster. Name object corresponds to the name of an XML or HTML tag in the original document.

Syntax:

tag.name
"""
"""# Import module
from bs4 import BeautifulSoup

# Initialize the object with an XML string
soup = BeautifulSoup(<root><name_of_tag>the first strong tag</name_of_tag></root>, "lxml")

# Get the tag
tag = soup.find('name_of_tag')

# Get the tag name
name = tag.name

# Print the output
print(name)
"""



"""# Import module
from bs4 import BeautifulSoup

# Initialize the object with a HTML page
soup = BeautifulSoup('''
	<html>
		<h2> Heading 1 </h2>
		<h1> Heading 2 </h1>
	</html>
	''', "lxml")

# Get the whole h2 tag
tag = soup.h2

# Get the name of the tag
name = tag.name

# Print the output
print(name)
"""


"""
# Contents list – Python Beautifulsoup
The contents list is provided by Beautiful Soup which is a web scraping framework for Python. Web scraping is the process of extracting data from the website using automated tools to make the process faster. The content is a list that contains the tag’s children.

Syntax: 

 tag.contents
"""


# Import Beautiful Soup
from bs4 import BeautifulSoup

# Create the document
doc = "<body><b> Hello world </b><body>"

# Initialize the object with the document
soup = BeautifulSoup(doc, "html.parser")

# Get the whole content from the body tag
contents = soup.body.contents

# Print the contents
print(contents)


# Import Beautiful Soup
from bs4 import BeautifulSoup

# Create the document
doc = "<body><b> Hello world </b><body>"

# Initialize the object with the document
soup = BeautifulSoup(doc, "html.parser")

# Get the whole content from the body tag
contents = soup.body.contents

# Print the type of contents
print(type(contents))


"""
# Scrapping the data of Flipkart
"""


import requests
from bs4 import BeautifulSoup as BS

link = 'https://www.flipkart.com/watches/pr?sid=r18'

flipkart_link = requests.get(link)

soup = BS(flipkart_link.text, 'html.parser')

elements = soup.find_all("div", class_="_1AtVbE")

for element in elements:
    if element:
        a = element.find("div", class_="_13oc-S _1t9ceu")
        if a:
            b = a.find("div", class_="_1xHGtK _373qXS")
            if b:
                c = b.find("div", class_="_2B099V")
                if c:
                    d = c.find("div", class_="_25b18c")
                    if d:
                        e = d.find("div", class_="_30jeq3")
                        if e:
                            print(e.text)
