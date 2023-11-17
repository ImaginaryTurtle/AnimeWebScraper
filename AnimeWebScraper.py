import FolderNames
import Scraper



if __name__ == "__main__":
    animeDict = FolderNames.create_anime_list()
    if animeDict:
        #Do Stuff
        print(animeDict)
    #Scraper.get_urls()
    #else:
    #    exit()
