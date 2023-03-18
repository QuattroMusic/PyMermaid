# +---------+
# | imports |
# +---------+
import PyMermaid.class_diagram.class_diagram as _internal

# +---------------+
# | add functions |  ->  returns an object
# +---------------+
def add_class(name: str) -> _internal.Class:
    """
    Undocumented
    """
    return _internal.Class(name=name)

#def link(a,b):
#    """
#    Undocumented
#    """
#    return _internal.link(a=a,b=b)

def evaluate():
    """
    Undocumented
    """
    return _internal.evaluate()

# +-----------+
# | constants |  ->  used instead of numbers inside functions
# +-----------+
