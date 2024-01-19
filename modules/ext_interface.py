import re

def get_solidity_interface(f: str):
    with open(f, 'r') as file:
        content = file.read()

        matches = re.findall(r" *?\/\*[\s\S]*?function[\s\S]*?{", content)

        return [f.replace(" {", ";") for f in matches if " public " in f or " external " in f]