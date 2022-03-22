# +---------+
# | imports |
# +---------+
import PyMermaid.flowchart._internal_flowchart as _internal
from typing import Union as _Union
from typing import List as _List
from typing import Tuple as _Tuple


# +---------------+
# | add functions |  ->  returns an object
# +---------------+
def add_group(name: str, direction: int = 0) -> _internal.Group:
    """
    ==========

    Basic Usage
    -----------
    Creates a group of nodes/links

    ==========

    Parameters:
    -----------
    name: Required, string
            Must to be unique
    direction: Optional, 0 <= int <= 3
            Changes direction of the nodes inside of the group\n
            Accepts costants (layout_...)\n
            Default value: 0

    ==========

    Returns:
    --------
    Group object, also used to make links

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> with f.add_group("one") as g1:
    >>>     n1 = f.add_node("test1",shape=f.nodeShape_cylindrical)
    >>>     n2 = f.add_node("test2")
    >>>     g1.add(f.link(n1,n2))

    Alternative usage, where you can link the entire group

    >>> from PyMermaid.mermaid import flowchart as f
    >>> with f.add_group("one") as g1:
    >>>     g1.add(f.link(f.add_node(),f.add_node()))
    >>> f.link(f.add_node(),g1)

    ==========
    """
    return _internal.Group(name=name, direction=direction)


def add_node(text: str = "", shape: int = 0, style: _internal.NodeStyle = "", customId: str = "") -> _internal.Node:
    """
    ==========

    Basic usage:
    ------------
    Creates a node, which can be linked to other nodes / groups

    ==========

    Parameters:
    -----------
    text: Optional, string
            The text displayed inside the node\n
            Default value: ''
    shape: Optional, 0 <= int <= 12
            Changes the shape of the node\n
            Accepts costants (nodeShape_...)\n
            Default value: 0
    style: Optional, Style object
            The style of the node\n
            See *add_style* for more info\n
    useNameAsId: Optional, string
            If not provided, the node id will be numeric\n
            If provided, the number will be replaced with the argument\n
            Must to be unique

    ==========

    Returns:
    --------
    Node object, used inside links

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> f.link(f.add_node(),f.add_node())

    Alternative usage, saves node as object

    >>> from PyMermaid.mermaid import flowchart as f
    >>> n1 = f.add_node(customId="test1")
    >>> n2 = f.add_node(customId="test2")
    >>> f.link(n1,n2)

    ==========
    """

    return _internal.Node(text=text, shape=shape, style=style, customId=customId)


def add_arrow(text: str = "", type: int = 0, length: int = 1, backArrow: bool = False) -> _internal.Arrow:
    """
    ==========

    Basic usage:
    ------------
    Creates an arrow object, used inside the links

    ==========

    Parameters:
    -----------
    name: Optional, string
            The text displyed inside of the arrow\n
            Default value: ''
    type: Optional, 0 <= int <= 5
            The type of the arrow\n
            Accepts constants (arrowType_...)\n
            Default value: 0
    length: Optional, int >= 1
            The length of the arrow\n
            Default value: 1
    backArrow: Optional, bool
            Default value: False

    ==========

    Returns:
    --------
    Arrow object, used inside links

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> a = f.add_arrow(type=f.arrowType_normalArrow)
    >>> f.link(f.add_node(),f.add_node(),a)

    Alternative usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> a = f.add_arrow(type=f.arrowType_thickArrow)
    >>> f.set_default_arrow(a)
    >>> f.link(f.add_node(),f.add_node())
    >>> f.link(f.add_node(),f.add_node())
    >>> #see set_default_value for more info

    ==========
    """
    return _internal.Arrow(text=text, type=type, length=length, backArrow=backArrow)


def add_node_style(name: str, fill: str = "", border_color: str = "", border_width: int = 1, text_color: str = "", dashed_border_lengths: _Union[_List[int], _Tuple[int]] = ()) -> _internal.NodeStyle:
    """
    ==========

    Basic usage:
    ------------
    Creates a style object, used inside the nodes\n
    Used to change node fill color, border width, border color, text color and measures of dashed border

    ==========

    Parameters:
    -----------
    name: Required, string
            The name given to the style\n
            Must to be unique\n
            If the name is *default*, then it will affects all the nodes
    fill: See below, hexadecimal
            The fill color of the node
    border_color: See below, hexadecimal
            The color of the border
    border_width: See below, int
            The width of the border, in pixels
    text_color: See below, hexadecimal
            The color of the text
    dashed_border_length: See below, list of int
            The first value represents the length of the line, in pixels\n
            The second value represents the length of the space between the lines, in pixels

    At least *one* parameter (name exclused) is required

    ==========

    Returns:
    --------
    Style object, used inside nodes

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> s = f.add_node_style("myStyle",fill="#995324")
    >>> f.add_node(style=s)

    >>> from PyMermaid.mermaid import flowchart as f
    >>> s = f.add_node_style("myStyle",dashed_border_lengths=[6,8])
    >>> f.add_node(style=s)

    ==========
    """
    return _internal.NodeStyle(name=name, fill=fill, border_color=border_color, border_width=border_width, text_color=text_color, dashed_border_lengths=dashed_border_lengths)


def add_link_style(line_color: str = "#d3d3d3", line_width: int = 2, text_color: str = "", dashed_line_lengths: _Union[_List[int], _Tuple[int]] = ()):
    """
    ==========

    Basic usage:
    ------------
    Creates a style object, used inside the links\n
    Used to change link line color, line width, text color and measures of dashed line

    ==========

    Parameters:
    -----------
    line_color: See below, hexadecimal
            The color of the line
    line_width: See below, hexadecimal
            The width of the line
    text_color: See below, int
            The color of the text
    dashed_line_lengths: See below, list of int
            The first value represents the length of the line, in pixels\n
            The second value represents the length of the space between the lines, in pixels

    At least *one* parameter (name exclused) is required

    ==========

    Returns:
    --------
    Style object, used inside nodes

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> s = f.add_link_style(line_color="#00ff00")
    >>> f.link(f.add_node(),f.add_node(),style=s)

    >>> from PyMermaid.mermaid import flowchart as f
    >>> s = f.add_link_style(dashed_line_lengths=[10,4])
    >>> f.link(f.add_node(),f.add_node(),style=s)

    ==========
    """
    return _internal.LinkStyle(line_color=line_color, line_width=line_width, text_color=text_color, dashed_line_lengths=dashed_line_lengths)


# +-------------------+
# | general functions |
# +-------------------+
def link(a: _Union[_internal.Node, _internal.Group, _List[_internal.Node], _List[_internal.Group], _Tuple[_internal.Node, ...], _Tuple[_internal.Group, ...]], b: _Union[_internal.Node, _internal.Group, _List[_internal.Node], _List[_internal.Group], _Tuple[_internal.Node, ...], _Tuple[_internal.Group, ...]], arrow: _internal.Arrow = "", style: _internal.LinkStyle = "") -> None:
    """
    ==========

    Basic usage:
    ------------
    Creates a link between nodes or groups

    ==========

    Parameters:
    -----------
    a: Required, Node / Group / list of Nodes / list of Group
            The first element linked to *b*
    b: Required, Node / Group / list of Nodes / list of Group
            The second element linked to *a*
    arrow: Optional, Arrow object
            The type of arrow whick links the two object
            Default value: a line

    ==========

    Returns:
    --------
    None

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> f.link(f.add_node(),f.add_node())

    Alternative usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> a = f.add_arrow(type=f.arrowType_thickArrow)
    >>> f.link(f.add_node()f.add_node(),a)

    ==========
    """
    return _internal.link(a=a, b=b, arrow=arrow, style=style)


def evaluate(toFile: bool = False, clear: bool = True) -> str:
    """
    ==========

    Basic usage:
    ------------
    Generate the mermaid code

    ==========

    Parameters:
    -----------
    toFile: Optional, bool
            Write the code to file, named 'output.md'\n
            Default value: False
    clear: Optional, bool
            Clear the code after calling the function
            Default value: True

    ==========

    Returns:
    --------
    The code, as a string

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> f.link(f.add_node(),f.add_node())
    >>> print(f.evaluate())

    ==========
    """
    return _internal.evaluate(toFile=toFile, clear=clear)


def comment(comment: str) -> None:
    """
    ==========

    Basic usage:
    ------------
    Adds a comment row inside the code

    ==========

    Parameters:
    -----------
    comment: Required, string
            The comment string

    ==========

    Returns:
    --------
    None

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> f.comment('Nodes')
    >>> n1 = f.add_node(shape=1)
    >>> n2 = f.add_node(shape=1)
    >>> f.comment('Links')
    >>> f.link(n1,n2)
    >>> print(f.evaluate())

    ==========
    """
    return _internal.comment(comment=comment)


def click(node: _internal.Node, link: str) -> None:
    """
    ==========

    Basic usage:
    ------------
    Adds a click callback\n
    When node is clicked, it opens the specified link

    ==========

    Parameters:
    -----------
    node: Required, Node object
            The node object which it can be clicked
    link: Required, string
            The browser page opened when pressed the node

    ==========

    Returns:
    --------
    None

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> n1 = f.add_node()
    >>> n2 = f.add_node()
    >>> f.link(n1,n2)
    >>> f.click(n1,'https://github.com/')
    >>> print(f.evaluate())

    ==========
    """
    return _internal.click(node=node, link=link)


def RGBtoHEX(r: _Union[_List[int], _Tuple[int, ...], int], g: int = 0, b: int = 0) -> str:
    """
    ==========

    Basic usage:
    ------------
    Converts the rgb value to hexadecimal

    ==========

    Parameters:
    -----------
    r: Required, int / list of int
            The red amount\n
            If *r* is a number, then they are required the other two parameters\n
            If *r* is a list, the other two parameters will be ignored
    g: Optional, int
            The green amount
    b: Optional, int
            The blue amount

    ==========

    Returns:
    --------
    The hexadecimal value, as a string

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> hex = f.RGBtoHEX(40,160,240)

    Alternative usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> hex = f.RGBtoHEX([40,160,240])

    ==========
    """
    return _internal.RGBtoHEX(r=r, g=g, b=b)


# +---------------+
# | set functions |
# +---------------+
def set_layout(direction: int) -> None:
    """
    ==========

    Basic usage:
    ------------
    Set the graph direction

    ==========

    Parameters:
    -----------
    direction: Required, 0 <= int <= 3
            The direction of the graph\n
            Accepts costants (layout_...)
            Default value: 0

    ==========

    Returns:
    --------
    None

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> f.set_layout(2)
    >>> f.link(f.add_node(),f.add_node())

    Alternative usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> f.set_layout(f.layout_leftToRight)
    >>> f.link(f.add_node(),f.add_node())

    Without using the function, the default value is 0

    >>> from PyMermaid.mermaid import flowchart as f
    >>> #f.set_layout(0)
    >>> f.link(f.add_node(),f.add_node())

    ==========
    """
    return _internal.set_layout(direction=direction)


def set_default_arrow(arrow: _internal.Arrow()) -> None:
    """
    ==========

    Basic usage:
    ------------
    Set the default arrow used inside links, without giving it every time

    ==========

    Parameters:
    -----------
    arrow: Required, Arrow object
            The arrow object used inside the links

    ==========

    Returns:
    --------
    None

    ==========

    Examples:
    ---------
    Basic usage

    >>> from PyMermaid.mermaid import flowchart as f
    >>> a = f.add_arrow(type=f.arrowType_thickArrow)
    >>> f.set_default_arrow(a)
    >>> f.link(f.add_node(),f.add_node())
    >>> f.link(f.add_node(),f.add_node())

    It's the same as writing

    >>> from PyMermaid.mermaid import flowchart as f
    >>> a = f.add_arrow(type=f.arrowType_thickArrow)
    >>> f.link(f.add_node(),f.add_node(),a)
    >>> f.link(f.add_node(),f.add_node(),a)

    ==========
    """
    return _internal.set_default_arrow(arrow=arrow)


# +-----------+
# | constants |  ->  used instead of numbers inside functions
# +-----------+
nodeShape_default = _internal.nodeShape_default
nodeShape_roundEdges = _internal.nodeShape_roundEdges
nodeShape_stadium = _internal.nodeShape_stadium
nodeShape_subroutine = _internal.nodeShape_subroutine
nodeShape_cylindrical = _internal.nodeShape_cylindrical
nodeShape_circle = _internal.nodeShape_circle
nodeShape_asymmetric = _internal.nodeShape_asymmetric
nodeShape_rhombus = _internal.nodeShape_rhombus
nodeShape_hexagon = _internal.nodeShape_hexagon
nodeShape_parallelogram = _internal.nodeShape_parallelogram
nodeShape_parallelogramAlt = _internal.nodeShape_parallelogramAlt
nodeShape_trapezoid = _internal.nodeShape_trapezoid
nodeShape_trapezoidAlt = _internal.nodeShape_trapezoidAlt

layout_topToBottom = _internal.layout_topToBottom
layout_bottomToTop = _internal.layout_bottomToTop
layout_leftToRight = _internal.layout_leftToRight
layout_rightToLeft = _internal.layout_rightToLeft

arrowType_normal = _internal.arrowType_normal
arrowType_normalArrow = _internal.arrowType_normalArrow
arrowType_thick = _internal.arrowType_thick
arrowType_thickArrow = _internal.arrowType_thickArrow
arrowType_dotted = _internal.arrowType_dotted
arrowType_dottedArrow = _internal.arrowType_dottedArrow
