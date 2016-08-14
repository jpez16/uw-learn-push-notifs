from flask import Flask
import re
import mechanize
app = Flask(__name__)

@app.route('/')
def scrap_learn():
    br = mechanize.Browser()
    br.open("http://learn.uwaterloo.ca")
    #so learn is open OR login screen is open
    #force login screen?
    return "yaaay"
