import os
import re

def getEnvFile():
    vars = {}
    with open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '.env'))) as file:
        for line in file:
            var = re.sub(r"[\n\t\s]*", "", line).split('=')
            if(len(var) > 1):
                key = var[0]
                val = var[1]
                vars[key] = val
    return vars
