from flask import Flask
from bs4 import BeautifulSoup
import re
import mechanize
app = Flask(__name__)

@app.route('/')
def scrape_learn():
    #remember to remove before commiting
    username = "None"
    password = "None"
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/534.3')]
    br.open("http://learn.uwaterloo.ca")
    br.select_form(nr=0)
    br["username"] = username
    #using raw text for now, will hash later
    br["password"] = password
    page = br.submit()
    page_html = BeautifulSoup(page, "html.parser")
    return page_html
