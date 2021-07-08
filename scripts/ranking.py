from sys import argv as args
from json import dumps, load

# Checa o arquivo json do usuário
try:
    open(f"info/{args[1]}.json")
except FileNotFoundError:
    open(f"info/{args[1]}.json", "w+").write('{"type": "normal"}')

userjson = load(open(f"info/{args[1]}.json", "r"))
try:
    int(userjson["points"])
except KeyError:
    userjson["points"] = 10


def mponto(pontos):
    global userjson
    userjson["points"] = int(userjson["points"]) + pontos
    open(f"info/{args[1]}.json", "w").write(dumps(userjson))


# Adiciona os pontos de comando
mponto(10)

try:
    if args[2] == "!":
        userjson["claims"] = 0
        userjson["points"] = userjson["points"] - int(float(args[3]))
        open(f"info/{args[1]}.json", "w").write(dumps(userjson))
        exit()
except IndexError:
    pass

# Checa quantas acs o usuário pode pegar com base nos pontos
userjson["claims"] = userjson["points"] / 1000
open(f"info/{args[1]}.json", "w").write(dumps(userjson))

# Aqui checa se o argumento para conquistas existe para prosseguir
try:
    mponto(int(args[2]))
except IndexError:
    exit()
