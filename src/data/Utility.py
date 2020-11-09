def extractGameFromURL(url):
    url = url.replace("https://www.nexusmods.com/","")
    i = 0
    game=""
    while url[i] != "/":
        game+=url[i]
        i+=1
    return game 
    
def extractIDFromURL(url):
    game = extractGameFromURL(url)
    return url.replace("https://www.nexusmods.com/"+game+"/mods/","")   

def extractGameAndIDFromURL(url):
    url = url.replace("https://www.nexusmods.com/","")
    i = 0
    game=""
    while url[i] != "/":
        game+=url[i]
        i+=1
    modID = url.replace(game+"/mods/","")
    return game, modID