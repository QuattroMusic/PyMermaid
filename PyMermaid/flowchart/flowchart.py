import PyMermaid.flowchart._internal_flowchart as _int
from enum import Enum as _Enum
from typing import Union as _Union, List as _List, Tuple as _Tuple


def add_group(text: str, direction: _int.Layout = _int.Layout.top_to_bottom) -> _int.Group:
    """
    Creates a group of nodes/links

    TODO
    """
    return _int.Group(text=text, direction=direction)


def add_node(text: str = "", shape: _int.NodeShapes = _int.NodeShapes.default, style: _int.NodeStyle = None) -> _int.Node:
    """
    Creates a node, which can be linked to other nodes / groups

    TODO
    """

    return _int.Node(text=text, shape=shape, style=style)


def add_arrow(text: str = "", type_: _int.ArrowType = _int.ArrowType.normal_arrow, length: int = 1, backArrow: bool = False) -> _int.Arrow:
    """
    Creates an arrow object, used inside the links

    TODO
    """
    return _int.Arrow(text=text, type_=type_, length=length, backArrow=backArrow)


def add_node_style(name: str, fill: str = "", border_color: str = "", border_width: int = 1, text_color: str = "", dashed_border_lengths: _Union[_List[int], _Tuple[int, int]] = ()) -> _int.NodeStyle:
    """
    Creates a style object, used inside the nodes\n
    Used to change node fill color, border width, border color, text color and measures of dashed border

    TODO
    """
    return _int.NodeStyle(name=name, fill=fill, border_color=border_color, border_width=border_width, text_color=text_color, dashed_border_lengths=dashed_border_lengths)


def add_link_style(line_color: str = "#d3d3d3", line_width: int = 2, text_color: str = "", dashed_line_lengths: _Union[_List[int], _Tuple[int, int]] = ()):
    """
    Creates a style object, used inside the links\n
    Used to change link line color, line width, text color and measures of dashed line

    TODO
    """
    return _int.LinkStyle(line_color=line_color, line_width=line_width, text_color=text_color, dashed_line_lengths=dashed_line_lengths)


def link(from_: _Union[_Union[_int.Node, _int.Group], _List[_Union[_int.Node, _int.Group]], _Tuple[_Union[_int.Node, _int.Group], ...]], to_: _Union[_Union[_int.Node, _int.Group], _List[_Union[_int.Node, _int.Group]], _Tuple[_Union[_int.Node, _int.Group], ...]], arrow: _int.Arrow = None, style: _int.LinkStyle = None):
    """
    Creates a link between nodes or groups

    TODO
    """
    return _int.link(from_=from_, to_=to_, arrow=arrow, style=style)


def evaluate() -> str:
    """
    Generate the mermaid code

    TODO
    """
    return _int.evaluate()


def set_layout(direction: _int.Layout) -> None:
    """
    Set the graph direction

    TODO
    """
    return _int.set_layout(direction=direction)


class NodeShapes(_Enum):
    default            = _int.NodeShapes.default
    round_edges        = _int.NodeShapes.round_edges
    stadium            = _int.NodeShapes.stadium
    subroutine         = _int.NodeShapes.subroutine
    cylindrical        = _int.NodeShapes.cylindrical
    circle             = _int.NodeShapes.circle
    asymmetric         = _int.NodeShapes.asymmetric
    rhombus            = _int.NodeShapes.rhombus
    hexagon            = _int.NodeShapes.hexagon
    parallelogram      = _int.NodeShapes.parallelogram
    parallelogram_alt  = _int.NodeShapes.parallelogram_alt
    trapezoid          = _int.NodeShapes.trapezoid
    trapezoid_alt      = _int.NodeShapes.trapezoid_alt


class Layout(_Enum):
    top_to_bottom = _int.Layout.top_to_bottom
    bottom_to_top = _int.Layout.bottom_to_top
    left_to_right = _int.Layout.left_to_right
    right_to_left = _int.Layout.right_to_left


class ArrowType(_Enum):
    normal        = _int.ArrowType.normal
    normal_arrow  = _int.ArrowType.normal_arrow
    thick         = _int.ArrowType.thick
    thick_arrow   = _int.ArrowType.thick_arrow
    dotted        = _int.ArrowType.dotted
    dotted_arrow  = _int.ArrowType.dotted_arrow
