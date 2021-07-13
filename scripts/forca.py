from json import dumps, load
from sys import argv as args
from random import choice, randint

session = args[1]
word = args[2].lower()
letrasub = False

if args[2] != "play":
    game = load(open(f"info/forca/{session}.json", "r"))
else:
    wlist = open("scripts/palavras/palavras.txt", "r").readlines()
    wordlist = []
    for indx in wlist:
        indx = (indx.lower()).replace("\n", "")
        wordlist.append(indx)
    game = {
        "word": choice(wordlist),
        "gamestatus": "ongoing",
        "letters": []
    }
    game["playerview"] = "_" * len(game['word'])
    game["tries"] = 10
    open(f"info/forca/{session}.json", "w+").write(dumps(game, indent=4))

if word != "play" and word != game["word"]:
    pview = [x for x in game["playerview"]]
    gword = game["word"]
    index = -1
    if len(word) == 1:
        for letra in gword:
            index += 1
            if letra == word:
                pview[index] = letra
                letrasub = True
        if not letrasub and word not in game["letters"]:
            game["tries"] -= 1
        
        game["letters"].append(word)

        if "_" not in pview:
            game["gamestatus"] = "defeat"
        
        if game["tries"] <= 0:
            game["gamestatus"] = "defeat"

        game["playerview"] = ''.join(pview)
    elif len(word) == 0:
        exit()
    else:
        game["tries"] -= 1
else:
    if word != "play":
        game["gamestatus"] = "victory"


open(f"info/forca/{session}.json", "w+").write(dumps(game, indent=4))
