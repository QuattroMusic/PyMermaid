import PyMermaid.internals.user_journey_diagram as _int
from typing import Union as _Union, List as _List, Tuple as _Tuple

def add_user(name: str) -> _int.User:
    """
    Undocumented
    """
    return _int.User(name=name)

def add_section(name: str) -> _int.Section:
    """
    Undocumented
    """
    return _int.Section(name=name)

def add_action(name: str, amount: int, users: _Union[_int.User, _List[_int.User], _Tuple[_int.User, ...]]) -> None:
    """
    Undocumented
    """
    return _int.add_action(name=name, amount=amount, users=users)


def evaluate() -> str:
    """
    Undocumented
    """
    return _int.evaluate()

def set_title(title: str) -> None:
    """
    Undocumented
    """
    return _int.set_title(title=title)
