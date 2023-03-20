import requests
from bs4 import BeautifulSoup

# send a GET request to the website
response = requests.get('https://www.fractalslab.com/courses/bangla-course-on-aws-serverless')

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find the page title
title = soup.title.string

# print the results
print(f'Title: {title}')



