import os
import requests
import shutil

def exporter(animeDict, directory):
    for anime in animeDict:
        if not os.path.exists(directory + "/" + anime['name'] + "/info"):
            os.mkdir(directory + "/" + anime['name'] + "/info")
        else:
            shutil.rmtree(directory + "/" + anime['name'] + "/info")
            os.mkdir(directory + "/" + anime['name'] + "/info")

        filepath = directory + "/" + anime['name'] + "/info/"

        info = open(filepath + "info.txt", "w", encoding="utf-8")

        info.writelines("Name:")
        info.writelines("\n" + anime['name'])
        info.writelines("\nURL:")
        info.writelines("\n" + (anime['url'] or "None"))

        info.writelines("\nIMG_File:")
        try:
            img = requests.get(anime['img'])
            open(filepath + anime['img'].split('/')[-1], 'wb').write(img.content)
            info.writelines("\n" + anime['img'].split('/')[-1])
        except:
            info.writelines("\nNone")

        info.writelines("\nRating:")
        info.writelines("\n" + (anime['rating'] or "None"))

        info.writelines("\nGenres:")
        if anime['genres']:
            for genre in anime['genres']:
                info.writelines("\n" + genre)
        else:
            info.writelines("\nNone")

        info.writelines("\nSynopsis:")
        try:
            info.writelines("\n" + (anime['synopsis'] or "None"))
        except:
            info.writelines("Error")

        info.writelines("\nEpisodes:")
        try:
            for episode in anime['episodes']:
                info.writelines("\n" + episode)
        except:
            info.writelines("\nNone")