import re

def getEnvFile():
    vars = {}
    with open('../.env') as file:
        for line in file:
            var = re.sub(r"[\n\t\s]*", "", line).split('=')
            key = var[0]
            val = var[1]
            vars[key] = val
