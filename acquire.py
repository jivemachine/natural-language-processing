from requests import get
from bs4 import BeautifulSoup
import os
import json



def get_article_text(url):
    url = url
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article_text = soup.find('div', itemprop='text').text
    article_header = soup.title.string
    
    blog_dict = {'title' : article_header, 'content' : article_text}
    
    return blog_dict

def store_blog_locally(blog_dict):
    with open('blog_post.txt', 'a') as f:
        f.write(json.dumps(blog_dict))
        

def get_blog_articles(url):
    blog_dict = get_article_text(url)
    store_blog_locally(blog_dict)
    blog_post = open('blog_post.txt', 'r')
    return blog_post.read()
    
    
    
    
    
    
    
    
    