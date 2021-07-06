from sys import argv as args
from json import dumps, load

# json base
basejson = {
    "help": "0",
    "teste": "0"
}

# Checa se já existe um arquivo json desse usuário
try:
    open(f"conquistas/{args[1]}.json")
except FileNotFoundError:

    # Se não, é criado
    genjson = dumps(basejson)
    open(f"conquistas/{args[1]}.json", "w+").write(genjson)

# Loada o arquivo json do usuário para fazer alterações nas conquistas
jeyson = open(f"conquistas/{args[1]}.json", "r")
loadjson = load(jeyson)

# Edita a key necessária de 0 para 1, assim realizando a conquista desejada
loadjson[args[2]] = "1"

# Salva em um arquivo json
open(f"conquistas/{args[1]}.json", "w+").write(dumps(loadjson))

