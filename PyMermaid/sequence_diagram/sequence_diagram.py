from . import _internal_sequence_diagram as _internal
from ._internal_sequence_diagram import UserType, ArrowType # used by users importing this file

def add_user(name: str, type: int = 0, customId: str = "") -> _internal.User:
    """
    Basic usage:
    ===========
    Creates and returns a user, an object who can have interactions on the graph

    ------------

    Parameters:
    ===========
    name:
        The string name given to the user, must be unique to avoid conflicts
    type: Optional
        Select between participant(default) or actor using the UserType enum
    customId: Optional
        Abbreviation shown in the final graph for the name, must be unique to avoid conflits

    ------------

    Examples:
    ===========
    Basic usage

    >>> from PyMermaid.mermaid import sequence_diagram as sd
    >>> sd.add_user("Alice")
    >>> print(sd.evaluate())

    Alternative usage

    >>> from PyMermaid.mermaid import sequence_diagram as sd
    >>> p1 = sd.add_user("Marco", UserType.ACTOR)
    >>> p2 = sd.add_user("Alice", UserType.ACTOR)
    >>> sd.link(p1, p2, sentence = 'Hi')
    >>> print(sd.evaluate())
    """
    return _internal.User(name=name, userType=type, customId=customId)


def link(userFrom: _internal.User, userTo: _internal.User, sentence: str = "", arrow_type: int = 1) -> None:
    """
    Basic usage:
    Creates a link between two input users

    -----------

    Parameters:
    ===========
    userFrom:
        First user object to start a link from
    userTo:
        Second user object to end a link to
    sentence:
        Optional string sentence to be written on top of the link
    arrow_type: Optional, int
        Optional type of arrow, bassed using the ArrowType enum\n
        Defaults to line with arrow

    ---------

    Examples:
    ===========
    Basic usage

    >>> from PyMermaid.mermaid import sequence_diagram as sd
    >>> p1 = sd.add_participant("Marco", type = 1)
    >>> p2 = sd.add_participant("Alice", type = 1)
    >>> sd.link(p1, p2, sentence = 'Hi Alice', arrow_type = sd.arrowType_open)
    >>> sd.link(p2, p1, sentence = 'Hi Marco', arrow_type = sd.arrowType_open)
    >>> print(sd.evaluate())

    """
    return _internal.link(userFrom, userTo, sentence=sentence, arrow_type=arrow_type)


def evaluate() -> str:
    """
    Generate and returns the mermaid code as a string
    
    Usage:
    ===========
    
    >>> from PyMermaid.mermaid import sequence_diagram as sd
    >>> sd.add_participant("Alice")
    >>> print(sd.evaluate())
    """
    return _internal.evaluate()