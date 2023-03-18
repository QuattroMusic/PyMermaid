# imports
from typing import Union, List, Tuple
from enum import Enum
from functools import partial


# constants
class NodeShapes(Enum):
    default = ("[", "]")
    round_edges = ("(", ")")
    stadium = ("([", "])")
    subroutine = ("[[", "]]")
    cylindrical = ("[(", ")]")
    circle = ("((", "))")
    asymmetric = (">", "]")
    rhombus = ("{", "}")
    hexagon = ("{{", "}}")
    parallelogram = ("[/", "/]")
    parallelogram_alt = ("[\\", "\\]")
    trapezoid = ("[/", "\\]")
    trapezoid_alt = ("[\\", "/]")
    double_circle = ("(((", ")))")


class Layout(Enum):
    top_to_bottom = "TB"
    bottom_to_top = "BT"
    left_to_right = "LR"
    right_to_left = "RL"


class ArrowType(Enum):
    normal = partial(lambda _back, length, text: ("-" * (length + 2)) + text)
    normal_arrow = partial(lambda back, length, text: back + ("-" * (length + 1)) + '>' + text)
    thick = partial(lambda _back, length, text: ("=" * (length + 2)) + text)
    thick_arrow = partial(lambda back, length, text: back + ("=" * (length + 1)) + '>' + text)
    dotted = partial(lambda _back, length, text: "-" + ("." * length) + '-' + text)
    dotted_arrow = partial(lambda back, length, text: back + "-" + ("." * length) + '->' + text)


# variables
nodes_id = -1
links_id = -1
flowchart_layout = "TB"

# code
code = []


def gen_id():
    global nodes_id
    nodes_id += 1
    return nodes_id


class NodeStyle:
    def __init__(self, name: str, fill: str = "", border_color: str = "", border_width: int = 1, text_color: str = "", dashed_border_lengths: Union[List[int], Tuple[int, int]] = ()):
        self.name: str = name
        self.fill: str = fill
        self.border_color: str = border_color
        self.border_width: int = border_width
        self.text_color: str = text_color
        self.dashed_border_lengths: tuple[str] = tuple(map(str, dashed_border_lengths))

        code.append(self)

class LinkStyle:
    def __init__(self, line_color: str = "#d3d3d3", line_width: int = 2, text_color: str = "", dashed_line_lengths: Union[List[int], Tuple[int, int]] = ()):
        self.line_color: str = line_color
        self.line_width: int = line_width
        self.text_color: str = text_color
        self.dashed_line_lengths: tuple[str] = tuple(map(str, dashed_line_lengths))

        code.append(self)

class Group:
    def __init__(self, text: str, direction: Layout = Layout.top_to_bottom):
        self.text = text
        self.direction = direction.value
        self._id = gen_id()

    def __enter__(self) -> 'Group':
        code.append(self)
        return self

    def __exit__(self, *_) -> None:
        code.append("__exit__")

    def __rshift__(self, other: Union[Union['Node', 'Group'], List[Union['Node', 'Group']], Tuple[Union['Node', 'Group'], ...]]) -> Union['Node', 'Group']:
        link(self, other)
        return other

class Node:
    def __init__(self, text: str = "", shape: NodeShapes = NodeShapes.default, style: NodeStyle = None):
        self.text = text
        self.shape = shape
        self.style = style
        self._id = gen_id()

        code.append(self)

    def __rshift__(self, other: Union[Union['Node', Group], List[Union['Node', Group]], Tuple[Union['Node', Group], ...]]) -> Union['Node', Group]:
        link(self, other)
        # with the return, you can do `Node1 >> Node2 >> Node3`
        return other

class Arrow:
    def __init__(self, text: str = "", type_: ArrowType = ArrowType.normal_arrow, length: int = 1, backArrow: bool = False):
        self.text = text
        self.type = type_
        self.length = length
        self.backArrow = backArrow

def add_node_style(item: NodeStyle, spacing: int = 0):
    args = []
    if item.fill != "":
        args.append(f"fill:{item.fill}")
    if item.border_color != "":
        args.append(f"stroke:{item.border_color}")
    if item.border_width != 1:
        args.append(f"stroke-width:{item.border_width}px")
    if item.text_color != "":
        args.append(f"color:{item.text_color}")
    if len(item.dashed_border_lengths) != 0:
        args.append(f"stroke-dasharray: {item.dashed_border_lengths[0]} {item.dashed_border_lengths[1]}")

    return f"{spacing * ' '} classDef {item.name} {','.join(args)}\n"

def add_link_style(item: LinkStyle):
    args = []

    if item.line_color != "":
        args.append(f"stroke:{item.line_color}")
    if item.line_width != 2:
        args.append(f"stroke-width:{item.line_width}")
    if item.text_color != "":
        args.append(f"color:{item.text_color}px")
    if len(item.dashed_line_lengths) != 0:
        args.append(f"stroke-dasharray:{item.dashed_line_lengths[0]} {item.dashed_line_lengths[1]}")

    code.append(f'linkStyle {links_id} ' + ','.join(args))

def add_group(item: Group, spacing: int = 0):
    return f'{spacing * " "}subgraph {item._id}["{item.text}"]\n{(spacing + 4) * " "}direction {item.direction}\n'

def add_node(item: Group, spacing: int = 0):
    if item.style is not None:
        return f'{spacing * " "}{item._id}{item.shape.value[0]}"{item.text}"{item.shape.value[1]}:::{item.style.name}\n'
    elif item.text == "":
        return f'{spacing * " "}{item._id}{item.shape.value[0]}" "{item.shape.value[1]}\n'
    return f'{spacing * " "}{item._id}{item.shape.value[0]}"{item.text}"{item.shape.value[1]}\n'

def add_arrow(item: Arrow):
    text = f'|"{item.text}"|' if item.text != "" else ""
    back = "<" if item.backArrow is True else ""
    return item.type.value(back, item.length, text)


def link(from_: Union[Union['Node', Group], List[Union['Node', Group]], Tuple[Union['Node', Group], ...]], to_: Union[Union['Node', Group], List[Union['Node', Group]], Tuple[Union['Node', Group], ...]], arrow: Arrow = None, style: LinkStyle = None):
    global links_id
    links_id += 1

    if arrow is None:
        arrow = Arrow()

    if type(from_) is list or type(from_) is tuple:
        from_ = " & ".join(map(str, [i._id for i in from_]))
    else:
        from_ = str(from_._id)

    if type(to_) is list or type(to_) is tuple:
        to_ = " & ".join(map(str, [i._id for i in to_]))
    else:
        to_ = str(to_._id)

    code.append(f"{from_} {add_arrow(arrow)} {to_}")

    if style is not None:
        add_link_style(style)


def evaluate() -> str:
    res = f"```mermaid\nflowchart {flowchart_layout}\n"
    spacing = 4

    for item in code:
        if type(item) == Group:
            res += add_group(item, spacing)
            spacing += 4

        elif type(item) == str and item == "__exit__":
            spacing -= 4
            res += f"{spacing * ' '}end\n"

        elif type(item) == Node:
            res += add_node(item, spacing)

        elif type(item) == NodeStyle:
            res += add_node_style(item, spacing)

        elif type(item) == str:
            # links and link styles
            res += f"{spacing * ' '}{item}\n"

    return res + "```"

def clear():
    global nodes_id, links_id, flowchart_layout
    # resets the code for generating a new one
    nodes_id = -1
    links_id = -1
    flowchart_layout = "TB"
    code.clear()


# def click_callback(node: Node, link: str):
#     code.append(f'click {node._id} "{link}"')
#
#
# def RGBtoHEX(r: Union[List[int], Tuple[int, ...], int], g: int = 0, b: int = 0) -> str:
#     hex = "#"
#     if type(r) is list or type(r) is tuple:
#         rgbList = r
#     else:
#         rgbList = [r, g, b]
#
#     for n in rgbList:
#         obj1 = n // 16
#         obj2 = n - obj1 * 16
#         if obj1 >= 10:
#             letters = ["a", "b", "c", "d", "e", "f"]
#             obj1 = letters[obj1 - 10]
#         if obj2 >= 10:
#             letters = ["a", "b", "c", "d", "e", "f"]
#             obj2 = letters[obj2 - 10]
#         hex += f"{obj1}{obj2}"
#
#     return hex


def set_layout(direction: Layout) -> None:
    global flowchart_layout

    flowchart_layout = direction.value
