# imports
from warnings import warn
from typing import Union, List, Tuple

# variables
sectionsNames = []

# code
code = []


class User:
    def __init__(self, name: str):
        self.name = name


class Section:
    def __init__(self, name: str):
        self.name = name
        self._times = 0
        self._canBeCalled = False

        if name in sectionsNames:
            warn("Duplicate name of the section", Warning, 3)
            exit()

        sectionsNames.append(name)

    def __enter__(self):
        code.append(f"section {self.name}")
        self._canBeCalled = True
        return self

    def __exit__(self, *args):
        self._canBeCalled = False
        if self._times == 0:
            warn("User added empty section or forget to use Section().add()", Warning, 3)
            while code[-1][0:7] != "section":
                code.pop(-1)
            code.pop(-1)

    def add(self, arg):
        self._times += 1
        if not self._canBeCalled:
            warn("Actions can be added only inside the section", Warning, 2)
            exit()


def add_action(name: str, amount: int, users: Union[User, List[User], Tuple[User, ...]]):
    if type(users) is list or type(users) is tuple:
        users = ", ".join(users.name)
    else:
        users = users.name
    code.append(f"{name}: {amount}: {users}")


def set_title(title: str):
    if len(code) == 0:
        code.append(f"title {title}")
    elif code[0][0:5] == "title":
        warn("The title has been yet set", Warning, 3)
        exit()
    else:
        warn("Set the title at the beginning of the code", Warning, 3)
        exit()


def evaluate():
    global code
    if len(code) == 0:
        warn("The code is empty", Warning, 3)
        exit()
    final = "```mermaid\njourney\n"
    spacing = 4
    firstSection = False

    for i in code:
        if i[0:7] == "section":
            if firstSection:
                spacing -= 4
            final += ' ' * spacing + i + "\n"
            spacing += 4
            firstSection = True
        else:
            final += ' ' * spacing + i + "\n"

    final += "```"

    return final
