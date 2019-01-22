#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
from secret import username, password

import os
#
# if "HTTP_COOKIE" in :
#     for cookie in map(string, split(environ['HTTP_COOKIE'], ';')):
#         (key, value) = split(cookie, '=')
#         if key == "username":
#             c_username = value
#         if key == "password":
#             c_password = value

# Return this to the webpage
print("Content-Type: text/html\r\n")
c_username = ""
c_password = ""
try:
    cookie_string = os.environ.get("HTTP_COOKIE")
    cookie_pairs = cookie_string.split(";") # gives me ["key=val"]
    for pair in cookie_pairs:
        key, val = pair.split("=")
        if "username" in key:
            c_username = val
        elif "password" in key:
            c_username = val
except:
    pass

if c_username == username and c_password == password:
    print("\r\n")
    print("<h1>" + os.environ.get("HTTP_COOKIE") + "</h1>")
    print(secret_page(c_username, c_password))
# Print form post data if method was POST
elif os.environ.get("REQUEST_METHOD", "GET") == "POST":
    form = cgi.FieldStorage()
    form_username = form.getvalue("username")
    form_password = form.getvalue("password")
    if form_username == username and form_password == password:
        print("Set-Cookie: username={};".format(username))
        print("Set-Cookie: password={};".format(password))
        print("\r\n")
        print(secret_page(username, password))
    else:
        print("\r\n")
        print(after_login_incorrect())
else:
    print("\r\n")
    print("<h1>" + os.environ.get("HTTP_COOKIE") + "</h1>")
    print(login_page())
