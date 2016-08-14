from flask import Flask
from bs4 import BeautifulSoup
import re
import mechanize
app = Flask(__name__)

@app.route('/')
def scrap_learn():
    #remember to remove before commiting
    username = "abc"
    password = "xyz"
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/534.3')]
    print "-1"
    br.open("http://learn.uwaterloo.ca")
    print "0"
    br.select_form(nr=0)
    br["username"] = username
    #using raw text for now, will hash later
    br["password"] = password
    print "1"
    br.submit()
    print "2"
    page = BeautifulSoup(br, "html.parser")
    print page

    #so learn is open OR login screen is open
    #force login screen?
    return "yaaay"
