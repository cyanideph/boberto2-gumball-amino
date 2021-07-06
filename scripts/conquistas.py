from sys import argv as args
from json import dumps, load
from os import system

# json base
basejson = {
    "author": f"{args[1]}"
}

# Checa se já existe um arquivo json desse usuário
try:
    open(f"conquistas/{args[1]}.json")
except FileNotFoundError:

    # Se não, é criado
    genjson = dumps(basejson)
    open(f"conquistas/{args[1]}.json", "w+").write(genjson)

if args[2] != "ignore":
    # Loada o arquivo json do usuário para fazer alterações nas conquistas
    jeyson = open(f"conquistas/{args[1]}.json", "r")
    loadjson = load(jeyson)

    # Edita a key necessária de 0 para 1, assim realizando a conquista desejada
    loadjson[args[2]] = "1"

    # Salva em um arquivo json
    open(f"conquistas/{args[1]}.json", "w+").write(dumps(loadjson))

system(f"python3 scripts/ranking.py {args[1]} {args[2]}")
