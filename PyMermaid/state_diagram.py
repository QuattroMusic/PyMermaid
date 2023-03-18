import PyMermaid.state_diagram.state_diagram as _internal
from typing import Union

def add_state(name: str, description: str = None) -> _internal.State:
    """
    Basic usage:
    ===========
    Creates and returns a State, an object who can have interactions on the graph

    ------------

    Parameters:
    ===========
    name:
        The string name given to the user, must be unique to avoid conflicts
    description: Optional
        optional description to give to the state

    ------------

    Examples:
    ===========
    Basic usage

    >>> from PyMermaid.mermaid import state_diagram as sd
    >>> add_state("still")
    >>> print(sd.evaluate())
    
    Alternative usage

    >>> from PyMermaid.mermaid import state_diagram as sd
    >>> s1 = State("still")
    >>> s2 = State("moving")
    >>> s3 = State("crash")
    >>> link_from_start(s1)
    >>> link_to_end(s1)
    >>> link_to_end(s3)
    >>> link(s1, s2)
    >>> link(s2, s3)
    >>> link(s2, s1)
    >>> print(evaluate())
    """
    return _internal.State(name=name,description=description)

def link_from_start(state: Union[_internal.State, str]) -> None:
    """
    Links a given state to the start node\n
    Alternatively creates and links a node from the start from the given string name
    """
    return _internal.link_from_start(state=state)
    
def link_to_end(state: Union[_internal.State, str]) -> None:
    """
    Links a given state to the end node\n
    Alternatively creates and links a node to the end from the given string name
    """
    return _internal.link_to_end(state=state)
    
def link(stateFrom: Union[_internal.State, str], stateTo: Union[_internal.State, str], text: str = None) -> None:
    """
    Links the given states (or strings) with an optional text between them
    """
    return _internal.link(stateFrom=stateFrom,stateTo=stateTo)

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
