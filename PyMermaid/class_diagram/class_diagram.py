# +---------+
# | imports |
# +---------+
import PyMermaid.class_diagram._internal_class_diagram as _internal

# +---------------+
# | add functions |  ->  returns an object
# +---------------+
def add_class(name: str) -> _internal.Class:
    """
    Undocumented
    """
    return _internal.Class(name=name)
