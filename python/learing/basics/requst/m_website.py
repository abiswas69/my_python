import requests

r= requests.get("https://www.google.com")
with open ("google.html",'w+') as f:
    f.write(r.text)