from bs4 import BeautifulSoup
import requests

HEADERS = {"User-Agent": "hi"}
req = requests.get("https://www.kanyetothe.com/forum/", headers=HEADERS, timeout=25)
#print(req)
soup = BeautifulSoup(req.text, "html.parser")

for a in soup.find_all('a', class_="aboardname"):
    print(a.text)
    print("Found the URL:", a['href']) 


    # thread class
    # subforum class
    # forum class