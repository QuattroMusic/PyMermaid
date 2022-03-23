# +---------+
# | imports |
# +---------+
import PyMermaid.sequence_diagram._internal_sequence_diagram as _internal


# +---------------+
# | add functions |  ->  returns an object
# +---------------+
def add_participant(name: str, type: int = 0, customId: str = "") -> _internal.Participant:
    """
    ==========

    Basic usage:
    ------------
    Creates a participant object\n
    It's the name of an object who can have interaction on the graph

    ==========

    Parameters:
    -----------
    name: Required, string
            The name given to the participant\n
            Must to be unique\n
            If it's given *customId*, then the second parameter must be unique
    type: Optional, 0 <= int <= 1
            Change between participant or actor\n
            Change the visual when evaluating the graph\n
            Accepts costants (participantType_...)\n
            Default value: participant (0)
    customId: Optional, string
            If given, must be unique\n
            Used only on the code for a shorter version of the name

    ==========

    Returns:
    --------
    Participant object

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import sequence_diagram as sd
    >>> sd.add_participant("Alice")
    >>> print(sd.evaluate())

    Alternative usage

    >>> from PyMermaid.mermaid import sequence_diagram as sd
    >>> p1 = sd.add_participant("Marco",type=1)
    >>> p2 = sd.add_participant("Alice",type=1)
    >>> sd.link(p1,p2,sentence='Hi')
    >>> print(sd.evaluate())

    ==========
    """
    return _internal.Participant(name=name, type=type, customId=customId)


# +-------------------+
# | general functions |
# +-------------------+
def link(a: _internal.Participant, b: _internal.Participant, sentence: str = "", arrow_type: int = 1) -> None:
    """
    ==========

    Basic usage:
    ------------
    Creates a link between two participants

    ==========

    Parameters:
    -----------
    a: Required, Participant object
            The first element linked to *b*
    b: Required, Participant object
            The second element linked to *a*
    sentence: Optional, string
            The sentence to be written on top of the link
    arrow_type: Optional, int
            The type of arrow
            Accepts costants (arrowType_...)\n
            Default value: line with arrow

    ==========

    Returns:
    --------
    None

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import sequence_diagram as sd
    >>> p1 = sd.add_participant("Marco",type=1)
    >>> p2 = sd.add_participant("Alice",type=1)
    >>> sd.link(p1,p2,sentence='Hi Alice',arrow_type=sd.arrowType_open)
    >>> sd.link(p2,p1,sentence='Hi Marco',arrow_type=sd.arrowType_open)
    >>> print(sd.evaluate())

    ==========
    """
    return _internal.link(a=a, b=b, sentence=sentence, arrow_type=arrow_type)


def evaluate() -> str:
    """
    ==========

    Basic usage:
    ------------
    Generate the mermaid code

    ==========

    Parameters:
    -----------
    None

    ==========

    Returns:
    --------
    The code, as a string

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import sequence_diagram as sd
    >>> sd.add_participant("Alice")
    >>> print(sd.evaluate())

    ==========
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
