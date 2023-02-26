# +---------+
# | imports |
# +---------+
import PyMermaid.state_diagram._internal_state_diagram as _internal
from typing import Union as _Union

# +---------------+
# | add functions |  ->  returns an object
# +---------------+
def State(name: str, description: str = None) -> _internal.State:
    """
    Undocumented
    """
    return _internal.State(name=name,description=description)

# +-------------------+
# | general functions |
# +-------------------+
def link_to_end(state: _Union["State", str]) -> None:
    """
    Undocumented
    """
    return _internal.link_to_end(state=state)

def link(stateFrom: _Union["State", str], stateTo: _Union["State", str], text: str = None) -> None:
    """
    Undocumented
    """
    return _internal.link(stateFrom=stateFrom,stateTo=stateTo)
def link_from_start(state: _Union["State", str]) -> None:
    """
    Undocumented
    """
    return _internal.link_from_start(state=state)

def evaluate() -> str:
    """
    Undocumented
    """
    return _internal.evaluate()
