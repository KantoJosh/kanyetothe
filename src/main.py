#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

HEADERS = {"User-Agent": "hi"}
# req = requests.get("https://www.kanyetothe.com/forum/", headers=HEADERS, timeout=25)
# soup = BeautifulSoup(req.text, "html.parser")

# for a in soup.find_all('a', class_="aboardname"):
#     print(a)
#     print(a.text)
#     print("Found the URL:", a['href']) 


    # thread class
    # subforum class
    # forum class
# TODO init with forum topic (forum/page/thread)
class Forum:
    def __init__(self,url):
        self._url = url
        req = requests.get(url, headers=HEADERS, timeout=25)
        self.soup = BeautifulSoup(req.text, "html.parser")
        self.page_limit = int(self.soup.find_all('a',class_='navPages')[-1].text)

        #each page adds 0.60 to end
    def get_subforums(self):
        subforums = []
        for a in self.soup.find_all('a', class_="aboardname"):
            print(f"{a.text}:", a['href'])
            subforums.append(Forum(a['href']))
        return subforums

    def threads(self,page = 1):
        if (page == 1):
            for count,thread in enumerate(self.soup.find_all('td',class_='topic_title')):
                print(f'{count}: {thread.find("a").text}')
        else:
            for row in self.soup.find_all('tr'):
                x = row.find('td',class_='num')
                if (x != None):
                    reply_count = int(x.text[:x.text.find(' ')])
                    print(x.text)
                    print(reply_count)
                    view_count = int(x.text[x.text.find('s')+1 : x.text.find('V') - 1])
                    print(view_count)
                
    

    def page_limit(self):
        print(self.soup.find_all('a',class_='navPages')[-1].text)


class Thread:
    def __init__(url):
        req = requests.get(url, headers=HEADERS, timeout=25)
        self.soup = BeautifulSoup(req.text, "html.parser")
    
    @property
    def reply_count():
        pass
    def view_count():
        pass
    def age():
        pass
    def most_recent_comment():
        pass # time,c

if __name__ == "__main__":
    f = Forum("https://www.kanyetothe.com/forum/index.php?board=1.0")
    f.threads(2)