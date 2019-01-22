#!/usr/bin/env python3

# Can allow us to see certain types of exceptions/errors in our script
import cgi
import cgitb
cgitb.enable()

import os
import json
from urllib.parse import parse_qs


# Return this to the webpage
print("Content-Type: text/html\n")
print()
print("<!doctype html>")
print("<head>")
print("<title>Hello</title>")
print("<style>pre {white-space: pre-wrap; word-wrap: break-word;}</style>")
print("</head>")
print("<h2>Hello World</h2>")

# Print query params
print("<dl>")
print("<dt>QUERY_STRING:</dt>")
print("<dd>")
print(parse_qs(os.environ.get("QUERY_STRING")))
print("</dd>")
print("<dt>HTTP_USER_AGENT:</dt>")
HTTP_USER_AGENT = os.environ.get("HTTP_USER_AGENT")
print(f"<dd>{HTTP_USER_AGENT}</dd>") # f-strings (a way to format)
print("</dl>")

#cgi.print_environ()
# Serve environment variables back as JSON
print("<pre>")
env_json = {}
for key, value in os.environ.items():
    env_json[key] = value
print(json.dumps(env_json))
print("</pre>")
