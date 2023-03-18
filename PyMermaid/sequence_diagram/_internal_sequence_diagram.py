from warnings import warn
from enum import Enum
    
class UserType(Enum):
    PARTICIPANT = 0
    ACTOR       = 1

class ArrowType(Enum):
    LINE         = 0
    ARROW        = 1
    CROSS        = 2
    OPEN         = 3
    DOTTED_LINE  = 4
    DOTTED_ARROW = 5
    DOTTED_CROSS = 6
    DOTTED_OPEN  = 7

participantNames = []
code = []

class User:
    def __init__(self, name: str, userType: UserType = UserType.PARTICIPANT, customId: str = ""):
        self.name: str = name
        self.userType: UserType = userType
        self.customId: str = customId

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

        if self.userType == UserType.PARTICIPANT:
            code.append(f"participant {self.name}{obj1}")
        elif self.userType == UserType.ACTOR:
            code.append(f"actor {self.name}{obj1}")
        else:
            warn("Type parameter must a UserType enum", Warning, 3)
            exit()


def link(a: User, b: User, sentence: str = "", arrow_type: ArrowType = ArrowType.ARROW) -> None:
    arrows = ["->", "->>", "-x", "-)", "-->", "-->>", "--x", "--)"]

    code.append(f"{a.customId}{arrows[arrow_type.value]}{b.customId}: {sentence}")


def evaluate() -> str:
    if len(code) == 0:
        warn("The code is empty", Warning, 3)
        exit()
    final = "```mermaid\nsequenceDiagram\n"
    spacing = 4

    for i in code:
        final += ' ' * spacing + i + "\n"

    final += "```"

    return final
    
if __name__ == "__main__":
    p1 = User("Marco", UserType.ACTOR)
    p2 = User("Alice", UserType.ACTOR)
    link(p1, p2, sentence = 'Hi Alice', arrow_type = ArrowType.CROSS)
    link(p2, p1, sentence = 'Hi Marco', arrow_type = ArrowType.OPEN)
    print(evaluate())