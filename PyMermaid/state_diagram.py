import PyMermaid.internals.state_diagram as _int
from typing import Union

def add_state(name: str, description: str = None) -> _int.State:
    """
    Undocumented
    """
    return _int.State(name=name,description=description)

def link_from_start(state: Union[_int.State, str]) -> None:
    """
    Undocumented
    """
    return _int.link_from_start(state=state)
    
def link_to_end(state: Union[_int.State, str]) -> None:
    """
    Undocumented
    """
    return _int.link_to_end(state=state)
    
def link(stateFrom: Union[_int.State, str], stateTo: Union[_int.State, str], text: str = None) -> None:
    """
    Undocumented
    """
    return _int.link(stateFrom=stateFrom,stateTo=stateTo)

def evaluate() -> str:
    """
    Undocumented
    """
    return _int.evaluate()
