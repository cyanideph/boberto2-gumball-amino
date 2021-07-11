from sys import argv as args
from json import load, dumps

try:
    jsonfile = load(open(f"info/{args[1]}.json", "r"))
    jsonfile["type"] = "staff"
    jsonfile["staff_type"] = args[2]
    open(f"info/{args[1]}.json", "w+").write(dumps(jsonfile))
except FileNotFoundError:
    staffjson = {
        "type": "staff",
        "staff_type": f"{args[2]}"
    }
    open(f"info/{args[1]}.json", "w+").write(dumps(staffjson))
