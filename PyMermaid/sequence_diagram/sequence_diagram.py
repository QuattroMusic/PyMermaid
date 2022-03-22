# +---------+
# | imports |
# +---------+
import PyMermaid.sequence_diagram._internal_sequence_diagram as _internal

# +---------------+
# | add functions |  ->  returns an object
# +---------------+
def add_participant(name:str, type: int = 0, customId: str = "") -> _internal.Participant:
    """
    Undocumented
    """
    return _internal.Participant(name=name,type=type,customId=customId)

# +-------------------+
# | general functions |
# +-------------------+
def link(a: _internal.Participant, b: _internal.Participant, sentence: str = "",arrow_type: int = 1) -> None:
    """
    Undocumented
    """
    return _internal.link(a=a,b=b,sentence=sentence,arrow_type=arrow_type)

def evaluate() -> str:
    """
    Undocumented
    """
    return _internal.evaluate()

# +-----------+
# | constants |  ->  used instead of numbers inside functions
# +-----------+
participantType_participant = _internal.participantType_participant
participantType_actor = _internal.participantType_actor

arrowType_line = _internal.arrowType_line
arrowType_arrow = _internal.arrowType_arrow
arrowType_cross = _internal.arrowType_cross
arrowType_open = _internal.arrowType_open
arrowType_dottedLine = _internal.arrowType_dottedLine
arrowType_dottedArrow = _internal.arrowType_dottedArrow
arrowType_dottedCross = _internal.arrowType_dottedCross
arrowType_dottedOpen = _internal.arrowType_dottedOpen
