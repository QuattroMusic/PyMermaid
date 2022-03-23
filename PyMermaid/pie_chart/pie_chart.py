# +---------+
# | imports |
# +---------+
import PyMermaid.pie_chart._internal_pie_chart as _internal


# +---------------+
# | add functions |  ->  returns an object
# +---------------+
def add_element(name: str, amount: float):
    """
    Undocumented
    """
    return _internal.add_element(name=name, amount=amount)


# +-------------------+
# | general functions |
# +-------------------+
def evaluate():
    """
    Undocumented
    """
    return _internal.evaluate()


# +---------------+
# | set functions |
# +---------------+
def set_title(title: str):
    """
    Undocumented
    """
    return _internal.set_title(title=title)
