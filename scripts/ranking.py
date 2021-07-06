from sys import argv as args

points = 0


def mponto(pontos):
    global points
    points += pontos
    open(f"pontos/{args[1]}", "w").write(str(points))


# Adiciona os pontos de comando
try:
    points = int(''.join(open(f"pontos/{args[1]}", "r").readlines()))
    points += 10
    open(f"pontos/{args[1]}", "w").write(str(points))
except FileNotFoundError:
    open(f"pontos/{args[1]}", "w+").write("10")

# Comandos de conquistas

# Aqui checa se o argumento para conquistas existe para prosseguir
try:
    if args[2]:
        conquista = args[2]
    if conquista == "ajuda_caralho":
        mponto(100)

except IndexError:
    exit()
