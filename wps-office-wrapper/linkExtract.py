#! /usr/bin/python3

from bs4 import BeautifulSoup, SoupStrainer

response=open("./download.html","r")

for link in BeautifulSoup(response,"html.parser", parse_only=SoupStrainer('a')):
 if link.has_attr('href'):
  if "download" in link['href'] and ( "https:" in link['href'] or "http:" in link['href']) and "kingsoftstore" not in link['href'] :
   print(link['href'])
