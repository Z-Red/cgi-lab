#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

# Return this to the webpage
print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
