#from http.client import responses
import requests
from bs4 import BeautifulSoup

def get_urls(animeDict):
#def get_urls():
    s = requests.session()

    postAddress = "https://www.animeftw.tv/index.php"
    payload = {"eolackset":"1"}
    
    s.post(postAddress,data=payload)

    address = "https://www.animeftw.tv/anime"

    page = s.get(address)
    html = BeautifulSoup(page.content, "html.parser")

    URLs = []
    
    
    #TODO: find animeDict[x]['Name'] on page, update animeDict[x]['URL']
    links = html.find_all("a")
    for link in links:
        try:
            if "/anime/" in link["href"]:
                URLs.append(link["href"])
        except:
            continue
        for anime in animeDict:
            if ''.join(filter(str.isalpha, anime["name"])).lower() == ''.join(filter(str.isalpha, link.text)).lower():
                anime["url"] = link["href"]

    
    
    #TESTING SECTION ------------------------------------------------------------------
    missingAnimes = []
    for anime in animeDict:
        if anime["url"] in URLs:
            URLs.remove(anime["url"])
        if anime["url"] == None:
            missingAnimes.append(anime["name"])


    print("Full List:")
    for anime in animeDict:
        print(anime["name"], anime["url"])
    print("\n\n\n\n\nMissing Animes:")
    for anime in missingAnimes:
        print(anime)
    print("\n\n\n\n\nMissing URLs:")
    for url in URLs:
        print(url)
    

    #TODO: Correct bug -> A Certain Magical Index        /anime/a-certain-magical-index2/
    #                     A Certain Magical Index 2      /anime/a-certain-magical-index2/


    #TODO: Use urls to get pages for each item, then update remaining information 
    #{'name':string, 'url':string, 'rating':string, 'genres':list[string], 'synopsis':string, 'episodes':list[string]}