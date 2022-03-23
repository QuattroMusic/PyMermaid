# +---------+
# | imports |
# +---------+
import PyMermaid.user_journey_diagram._internal_user_journey as _internal
from typing import Union as _Union
from typing import List as _List
from typing import Tuple as _Tuple


# +---------------+
# | add functions |  ->  returns an object
# +---------------+
def add_user(name: str) -> _internal.User:
    """
    Undocumented
    """
    return _internal.User(name=name)


def add_section(name: str) -> _internal.Section:
    """
    Undocumented
    """
    return _internal.Section(name=name)


def add_action(name: str, amount: int, users: _Union[_internal.User, _List[_internal.User], _Tuple[_internal.User, ...]]) -> None:
    """
    Undocumented
    """
    return _internal.add_action(name=name, amount=amount, users=users)


# +-------------------+
# | general functions |
# +-------------------+
def evaluate() -> str:
    """
    Undocumented
    """
    return _internal.evaluate()


# +---------------+
# | set functions |
# +---------------+
def set_title(title: str) -> None:
    """
    Undocumented
    """
    return _internal.set_title(title=title)
