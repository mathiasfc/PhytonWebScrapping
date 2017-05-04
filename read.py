#import requests
#from lxml import html
from bs4 import BeautifulSoup
import requests
import mechanize
import urllib2 
import cookielib

#url = "http://megatibia.com/?subtopic=accountmanagement"

#r  = requests.get(url)
#data = r.text
#soup = BeautifulSoup(data)

#for link in soup.find_all('a'):
#print(soup.prettify())

#--------------------




cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open(url)

#for f in br.forms():
#    print f
#print br.response().read()

print br.select_form(name="account_login=")

#br.select_form(nr=0)
#br.form['account_login'] = 'username'
#br.form['password_login'] = 'password.'
#br.submit()
#print br.response().read()