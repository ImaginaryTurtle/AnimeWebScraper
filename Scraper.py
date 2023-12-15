from ast import Try
import requests
from bs4 import BeautifulSoup
import fnmatch

def get_urls(animeDict):
    s = requests.session()

    postAddress = "https://www.animeftw.tv/index.php"
    payload = {"eolackset":"1"}
    
    s.post(postAddress,data=payload)

    address = "https://www.animeftw.tv/anime"

    page = s.get(address)
    html = BeautifulSoup(page.content, "html.parser")

    URLs = []
    

    links = html.find_all("a")
    for link in links:
        try:
            if "/anime/" in link["href"]:
                URLs.append(link["href"])
        except:
            continue
        for anime in animeDict:
            if ''.join(filter(str.isalnum, anime["name"])).lower() == ''.join(filter(str.isalnum, link.text)).lower():
                anime["url"] = link["href"]

    
    for anime in animeDict:
        if anime["url"]:
            animePage = s.get("https://www.animeftw.tv" + anime["url"])
            animeHtml = BeautifulSoup(animePage.content, "html.parser")

            animeImgs = animeHtml.find_all("img")
            animeGenres = animeHtml.find_all("a")
            animeSynopsis = animeHtml.find_all("div")

            for a in animeGenres:
                try:
                    if fnmatch.fnmatch(a["href"], "/anime/sort/?*"):
                        anime["genres"].append(a["href"][12:])
                except:
                    continue
            
            try:
                for a in animeImgs:
                    if "https://animeftw.tv/images/seriesimages/" in a["src"]:
                        anime["img"] = a["src"]
                    if "https://animeftw.tv/images/ratings/" in a["src"]:
                        anime["rating"] = a["src"][35:38]
            except:
                continue

            synopsisFound = False

            for a in animeSynopsis:
                if "Series Synopsis:" == a.text:
                    synopsisFound = True
                    continue
                if synopsisFound:
                    anime["synopsis"] = a.text
                    break

            episodesFound = False
            for a in animeSynopsis:
                if "Episodes:" == a.text or "Movies:" == a.text:
                    episodesFound = True
                    continue
                if episodesFound:
                    anime["episodes"]=list(filter(None, a.text.replace("\t","").split("\n")))
                    break