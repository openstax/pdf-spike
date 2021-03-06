import json
import sys


def msg(msg, *args, **kwargs):
    if args or kwargs:
        msg = msg.format(*args, **kwargs)
    print(msg, file=sys.stderr)

def write_file(filepath, data):
    if filepath.endswith(".json"):
        with open(filepath, "w") as file:
            json.dump(data, file)
    else:
        with open(filepath, "w") as file:
            file.write(data)
