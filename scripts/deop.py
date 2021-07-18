from json import dumps, load
from sys import argv as args


userjson = load(open(f"info/{args[1]}.json", "r"))

userjson["type"] = "normal"
userjson["staff_type"] = None

open(f"info/{args[1]}.json", "w").write(dumps(userjson))
