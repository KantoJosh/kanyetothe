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
# TODO init with forum topic
class Forum:
    def __init__(self,url):
        req = requests.get(url, headers=HEADERS, timeout=25)
        self.soup = BeautifulSoup(req.text, "html.parser")
        #self.sub_forums -- to find this, do same thing as above with for loop
        #self._url  -- get from parameter
        #each page adds 0.60 to end
    def get_sub_forums(self):
        for a in soup.find_all('a', class_="aboardname"):
            print(f"{a.text}:", a['href'])

    # TODO get thread by page number
    def get_threads(self,page = 1):
        if (page == 1):
            for count,thread in enumerate(self.soup.find_all('td',class_='topic_title')):
                print(f'{count}: {thread.find("a").text}')
        else:
            # make another req to appropriate site


class Thread:
    def __init__(url):
        req = requests.get(url, headers=HEADERS, timeout=25)
        self.soup = BeautifulSoup(req.text, "html.parser")
    
    @property
    def reply_count():
        pass


if __name__ == "__main__":
    f = Forum("https://www.kanyetothe.com/forum/index.php?board=6.0")
    #f.get_threads()
