from sys import argv as args

try:
    points = int(''.join(open(f"pontos/{args[1]}", "r").readlines()))
    points += 10
    open(f"pontos/{args[1]}", "w").write(str(points))
    print(points)
except FileNotFoundError:
    open(f"pontos/{args[1]}", "w+").write("10")
    print(points)

exit()
