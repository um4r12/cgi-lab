#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()
import os

from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie

print("Content-Type: text/html")
#print()
#print("<!doctype html><title>Hello</title><h2>Hello World</h2>")

#question 1
#print(os.environ)

#question 2
#print(os.environ["QUERY_STRING"])

#question 3
#print(os.environ["HTTP_USER_AGENT"])

#question 4
print(login_page())
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")


