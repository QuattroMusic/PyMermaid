import PyMermaid.internals.sequence_diagram as _int

def add_user(name: str, type: int = 0, customId: str = "") -> _int.User:
    """
    Undocumented
    """
    return _int.User(name=name, userType=type, customId=customId)

def link(userFrom: _int.User, userTo: _int.User, sentence: str = "", arrow_type: int = 1) -> None:
    """
    Undocumented
    """
    return _int.link(userFrom, userTo, sentence=sentence, arrow_type=arrow_type)

def evaluate() -> str:
    """
    Undocumented
    """
    return _int.evaluate()
