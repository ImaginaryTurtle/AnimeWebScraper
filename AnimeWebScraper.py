import FolderNames
import Scraper
import ExportData



if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    animeDict = FolderNames.create_anime_list(directory)
    if animeDict:
        animeDict = Scraper.get_urls(animeDict)
        ExportData.exporter(animeDict, directory)
    else:
        exit()
