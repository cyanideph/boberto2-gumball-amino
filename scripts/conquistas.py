from sys import argv as args
from json import dumps, load
from os import system

basejson = {}

# Checa se já existe um arquivo json desse usuário
try:
    open(f"info/{args[1]}.json")
except FileNotFoundError:
    # Se não, é criado
    genjson = dumps(basejson)
    open(f"info/{args[1]}.json", "w+").write(genjson)

if args[2] != "ignore":
    # Loada o arquivo json do usuário para fazer alterações nas conquistas
    jeyson = open(f"info/{args[1]}.json", "r")
    loadjson = load(jeyson)

    # Adiciona a conquista a lista de conquistas do usuário
    try:
        loadjson["achievements"].append(args[2])
    except KeyError:
        loadjson["achievements"] = [args[2]]

    # Salva em um arquivo json
    open(f"info/{args[1]}.json", "w+").write(dumps(loadjson))

system(f"python3 scripts/ranking.py {args[1]} {args[3]}")
