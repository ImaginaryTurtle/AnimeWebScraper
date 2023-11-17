from http.client import responses
import requests

def get_urls(animeDict):
    s = requests.session()

    postAddress = "https://www.animeftw.tv/index.php"
    payload = {"eolackset":"1"}
    
    s.post(postAddress,data=payload)

    address = "https://www.animeftw.tv/anime"

    page = s.get(address)

    #TODO: find animeDict[x]['Name'] on page, update animeDict[x]['URL']
    #TODO: Use urls to get pages for each item, then update remaining information 
    #{'name':string, 'url':string, 'rating':string, 'genres':list[string], 'synopsis':string, 'episodes':list[string]}

    print(page.text)