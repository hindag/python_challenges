import urllib.request, urllib.error, urllib.parse
import re

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827"

response = urllib.request.urlopen(url)
webContent = response.read()
webContent=webContent.decode("utf-8")

result=re.search(r'\d+',webContent)

final=result.group()

