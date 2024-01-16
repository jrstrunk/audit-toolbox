def get_solidity_interface(f: string):
    with open(file_path, 'r') as file:
        content = file.read()
        matches = re.findall("function.*?{", content)

        return [f.replace(" {", "") for f in matches if " public " in f or " external " in f]