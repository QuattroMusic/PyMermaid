# import
from warnings import warn

# costants
participantType_participant = 0
participantType_actor = 1

arrowType_line = 0
arrowType_arrow = 1
arrowType_cross = 2
arrowType_open = 3
arrowType_dottedLine = 4
arrowType_dottedArrow = 5
arrowType_dottedCross = 6
arrowType_dottedOpen = 7

# variables
participantNames = []

# code
code = []


class Participant:
    def __init__(self, name: str, type: int = 0, customId: str = ""):
        self.name = name
        self.type = type
        self.customId = customId

        self._addToCode()

    def _addToCode(self):
        obj1 = ""

        if self.customId != "":
            obj1 = f" as {self.name}"
            self.name = self.customId
        else:
            self.customId = self.name

        if self.name in participantNames:
            warn("Unable to put two partecipants with the same name", Warning, 4)
            exit()

        participantNames.append(self.name)

        if self.type == 0:
            code.append(f"participant {self.name}{obj1}")
        elif self.type == 1:
            code.append(f"actor {self.name}{obj1}")
        else:
            warn("Type parameter must be 0 or 1", Warning, 3)
            exit()


def link(a: Participant, b: Participant, sentence: str = "", arrow_type: int = 1) -> None:
    arrows = ["->", "->>", "-x", "-)", "-->", "-->>", "--x", "--)"]

    code.append(f"{a.customId}{arrows[arrow_type]}{b.customId}: {sentence}")


def evaluate() -> str:
    global code
    if len(code) == 0:
        warn("The code is empty", Warning, 3)
        exit()
    final = "```mermaid\nsequenceDiagram\n"
    spacing = 4

    for i in code:
        final += ' ' * spacing + i + "\n"

    final += "```"

    return final
