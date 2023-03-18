# imports
from warnings import warn

# variables
elementNames = []

# code
code = []


def add_element(name: str, amount: float) -> None:
    if name in elementNames:
        warn("Element already present", Warning, 3)
        exit()

    elementNames.append(name)

    code.append(f'"{name}": {amount}')


def evaluate():
    global code
    if len(code) == 0:
        warn("The code is empty", Warning, 3)
        exit()
    final = "```mermaid\npie\n"
    spacing = 4

    for i in code:
        final += ' ' * spacing + i + "\n"

    final += "```"

    return final


def set_title(title: str):
    if len(code) == 0:
        code.append(f"title {title}")
    elif code[0][0:5] == "title":
        warn("The title has been yet set", Warning, 3)
        exit()
    else:
        warn("Set the title at the beginning of the code", Warning, 3)
        exit()
