from json import load, dumps
import json
from sys import argv as args

# Cria uma enquete
if args[1] == "criar":
    enquete = {}

    for l in args[3:]:
        enquete[l] = 0
    
    # JSON enquete
    jsonpoll = dumps(enquete)
    open(f"enquetes/{args[2]}.json", "w+").write(jsonpoll)

# vota na enquete com o ID especificado
elif args[1] == "votar":
    jsonpoll = load(open(f"enquetes/{args[2]}.json", "r"))
    jsonpoll[args[3]] += 1
    jsonpoll = dumps(jsonpoll)
    open(f"enquetes/{args[2]}.json", "w+").write(jsonpoll)
