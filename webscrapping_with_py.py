"""
Making a Request

Python requests module has several built-in methods to make HTTP requests to specified URI using GET, POST, PUT, PATCH, or HEAD requests. A HTTP request is meant to either retrieve data from a specified URI or to push data to a server. It works as a request-response protocol between a client and a server. Here we will be using the GET request. 

GET method is used to retrieve information from the given server using a given URI. The GET method sends the encoded user information appended to the page request. 
"""

from aiohttp import request
import requests
req1 = requests.get('https://www.youtube.com/')

print("\n",req1)

print("\n",req1.content)


"""
# Response object
 
When one makes a request to a URI, it returns a response. This Response object in terms of python is returned by requests.method(), method being – get, post, put, etc. Response is a powerful object with lots of functions and attributes that assist in normalizing data or creating ideal portions of code. For example, response.status_code returns the status code from the headers itself, and one can check if the request was processed successfully or not.

Response objects can be used to imply lots of features, methods, and functionalities.
"""

#import module
import requests as rq
#making a get request
req2 = rq.get('https://www.facebook.com/')
#printing  request object
print("\n",req2.url)
#printing the request code
print("\n",req2.status_code)

"""
# Inspecting Website
 

Before getting out any information from the HTML of the page, we must understand the structure of the page. This is needed to be done in order to select the desired data from the entire page. We can do this by right-clicking on the page we want to scrape and select inspect element.

 


![image.png](attachment:image.png)

After clicking the inspect button the Developer Tools of the browser gets open. Now almost all the browsers come with the developers tools installed, and we will be using Chrome for this tutorial. 

 


 ![image-2.png](attachment:image-2.png)

The developer’s tools allow seeing the site’s Document Object Model (DOM). If you don’t know about DOM then don’t worry just consider the text displayed as the HTML structure of the page.


# Parsing the HTML
 

After getting the HTML of the page let’s see how to parse this raw HTML code into some useful information. First of all, we will create a BeautifulSoup object by specifying the parser we want to use.

 

Note: BeautifulSoup library is built on top of the HTML parsing libraries like html5lib, lxml, html.parser, etc. So BeautifulSoup object and specify the parser library can be created at the same time.
"""

import requests as rq
from bs4 import BeautifulSoup

#making a get reques
req3 = rq.get('https://www.geeksforgeeks.org/')

#printing the response received
print("\n",req3)

#parsing the html
pr_html = BeautifulSoup(req3.content,'html.parser')
print("\n",pr_html.prettify())


"""
This information is still not useful to us, let’s see another example to make some clear picture from this. Let’s try to extract the title of the page.
"""

import requests as rq
from bs4 import BeautifulSoup

#making a get reques
req4 = rq.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')

#parsing the html
pr_html = BeautifulSoup(req4.content,'html.parser')

#extracting the title tag
print("\n",pr_html.title)

#extracting the name of the tag
print("\n",pr_html.title.name)

#extracting the name of the parent tag
print("\n",pr_html.title.parent.name)


"""
# Finding Elements
Now, we would like to extract some useful data from the HTML content. The soup object contains all the data in the nested structure which could be programmatically extracted. The website we want to scrape contains a lot of text so now let’s scrape all those content. First, let’s inspect the webpage we want to scrape. 

![image.png](attachment:image.png)

Finding Elements by class
In the above image, we can see that all the content of the page is under the div with class entry-content. We will use the find class. This class will find the given tag with the given attribute. In our case, it will find all the div having class as entry-content. We have got all the content from the site but you can see that all the images and links are also scraped. So our next task is to find only the content from the above-parsed HTML. On again inspecting the HTML of our website – 

![image-2.png](attachment:image-2.png)
"""

import requests
from bs4 import BeautifulSoup

# Making a GET request
req5 = requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')

# Parsing the HTML
pr_html2 = BeautifulSoup(req5.content, 'html.parser')

s = pr_html2.find('div', class_='entry-content')
if s is not None:
    content = s.find_all('p')
    print(content)
else:
    print("\nNo matching element found.")



import requests
from bs4 import BeautifulSoup


# Making a GET request
req6 = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Parsing the HTML
soup = BeautifulSoup(req6.content, 'html.parser')

s = soup.find('div', class_='entry-content')
content = s.find_all('p')

print("\n",content)




