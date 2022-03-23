# imports
from typing import Union, List, Tuple
from warnings import warn

# constants
nodeShape_default = 0
nodeShape_roundEdges = 1
nodeShape_stadium = 2
nodeShape_subroutine = 3
nodeShape_cylindrical = 4
nodeShape_circle = 5
nodeShape_asymmetric = 6
nodeShape_rhombus = 7
nodeShape_hexagon = 8
nodeShape_parallelogram = 9
nodeShape_parallelogramAlt = 10
nodeShape_trapezoid = 11
nodeShape_trapezoidAlt = 12

layout_topToBottom = 0
layout_bottomToTop = 1
layout_leftToRight = 2
layout_rightToLeft = 3

arrowType_normal = 0
arrowType_normalArrow = 1
arrowType_thick = 2
arrowType_thickArrow = 3
arrowType_dotted = 4
arrowType_dottedArrow = 5

# variables
nodesId = -1
linksId = -1
groupsNames = []
nodesIds = []
unlinkedNodes = []

# code
code = []


class NodeStyle:
    def __init__(self, name: str, fill: str = "", border_color: str = "", border_width: int = 1, text_color: str = "", dashed_border_lengths: Union[List[int], Tuple[int]] = ()):

        if fill == "" and border_color == "" and border_width == 1 and text_color == "" and dashed_border_lengths == (5, 5):
            warn("At least one parameter is required", Warning, 3)
            exit()

        self.name = name
        self.fill = fill
        self.border_color = border_color
        self.border_width = border_width
        self.text_color = text_color
        self.dashed_border_lengths = list(map(str, dashed_border_lengths))

        self._addToCode()

    def _addToCode(self):
        obj = []
        if self.fill != "":
            obj.append(f"fill:{self.fill}")
        if self.border_color != "":
            obj.append(f"stroke:{self.border_color}")
        if self.border_width != 1:
            obj.append(f"stroke-width:{self.border_width}px")
        if self.text_color != "":
            obj.append(f"color:{self.text_color}")
        if self.dashed_border_lengths != []:
            obj.append(f"stroke-dasharray:{' '.join(self.dashed_border_lengths)}")
        code.append(f"classDef {self.name} {','.join(obj)}")


class LinkStyle:
    def __init__(self, line_color: str = "#d3d3d3", line_width: int = 2, text_color: str = "", dashed_line_lengths: Union[List[int], Tuple[int]] = ()):
        if line_color == "#d3d3d3" and line_width == 2 and text_color == "" and dashed_line_lengths == (5, 5):
            warn("At least one parameter is required", Warning, 3)
            exit()

        self.line_color = line_color
        self.line_width = line_width
        self.text_color = text_color
        self.dashed_line_lengths = list(map(str, dashed_line_lengths))

        self._addToCode()

    def _addToCode(self):
        obj = []
        if self.line_color != "":
            obj.append(f"stroke:{self.line_color}")
        if self.line_width != 2:
            obj.append(f"stroke-width:{self.line_width}")
        if self.text_color != "":
            obj.append(f"color:{self.text_color}px")
        if self.dashed_line_lengths != []:
            obj.append(f"stroke-dasharray:{' '.join(self.dashed_line_lengths)}")
        self.parameters = ','.join(obj)
        # code.append(f"classDef {self.name} {','.join(obj)}")


class Group:
    def __init__(self, name: str, direction: int = 0):
        self._id = name
        self.direction = direction
        self._canBeCalled = False
        self._times = 0

        if name in groupsNames:
            warn("Unable to put two different groups with same name", Warning, 3)
            exit()
        if name in nodesIds:
            warn("Unable to have a group name the same as a node", Warning, 3)
            exit()
        groupsNames.append(name)

    def __enter__(self):
        self._canBeCalled = True
        code.append(f"subgraph {self._id}")

        directions = ["TB", "BT", "LR", "RL"]

        code.append(f"direction {directions[self.direction]}")
        return self

    def __exit__(self, *_):
        self._canBeCalled = False
        # if it's empty

        code.append("end")
        if self._times == 0:
            warn("User added empty group or forget to use Group().add()", Warning, 3)
            while code[-1][0:8] != "subgraph":
                code.pop(-1)
            code.pop(-1)

    def add(self, arg):
        self._times += 1
        if not self._canBeCalled:
            warn("Links or nodes can be added only inside the group", Warning, 2)
            exit()
        if self._id in code[-1]:
            warn("Unable to link group to itself", Warning, 2)
            exit()


class Node:
    def __init__(self, text: str = "", shape: int = 0, style: NodeStyle = "", customId: str = ""):
        self.text = text
        self.shape = shape
        self.style = style
        self.customId = customId

        self._check()

    def _check(self):
        # check nodes with same id
        if self.customId == "":
            id = self._get_id()
            if id in nodesIds:
                warn("Unable to put two nodes with the same id", Warning, 3)
                exit()
            self._id = id
        else:
            if self.customId in nodesIds:
                warn("Unable to put two nodes with the same id", Warning, 3)
                exit()
            if self.customId in groupsNames:
                warn("Unable to have a node name the same as a group", Warning, 3)
                exit()
            self._id = self.customId

        # add node to code
        nodesIds.append(self._id)
        unlinkedNodes.append(self)
        self._addToCode()

    def _addToCode(self) -> None:
        if "\n" in self.text:
            self.text = self.text.replace("\n", "<br>")

        shapes = [["[", "]"], ["(", ")"], ["([", "])"], ["[[", "]]"], ["[(", ")]"], ["((", "))"], [">", "]"],
                  ["{", "}"], ["{{", "}}"], ["[/", "/]"], ["[\\", "\\]"], ["[/", "\\]"], ["[\\", "/]"]]

        # compute all cases of the parameters, simplified
        obj = ""
        if self.text == "":
            if self.shape == 0:
                obj = self._id
            else:
                obj = f'{self._id}{shapes[self.shape][0]}"{self._id}"{shapes[self.shape][1]}'

        if self.text != "":
            obj = f'{self._id}{shapes[self.shape][0]}"{self.text}"{shapes[self.shape][1]}'

        if self.style != "":
            obj += f":::{self.style.name}"

        code.append([obj, self])

    def _get_id(self) -> str:
        global nodesId
        nodesId += 1
        return str(nodesId)


class Arrow:
    def __init__(self, text: str = "", type: int = 0, length: int = 1, backArrow: bool = False):
        self.text = text
        self.type = type
        self.length = length
        self.backArrow = backArrow

        if "\n" in self.text:
            self.text = self.text.replace("\n", "<br>")

        assert (0 <= self.type <= 5)
        assert (self.length >= 1)

    def _gen(self) -> str:
        types = [["", "-", "--"], ["<", "-", "->"], ["", "=", "=="], ["<", "=", "=>"], ["", ".", "-"], ["<", ".", "->"]]

        arr = [types[self.type][1] for _ in range(self.length)] + [types[self.type][2]]

        # if there is no name, no need to put it
        if self.text == "":
            arr.append('')
        else:
            arr.append(f'|"{self.text}"|')

        # only affects arrows with > symbol
        if self.backArrow and self.type not in [0, 2, 4]:
            arr.insert(0, types[self.type][0])

        return ''.join(arr)


defaultArrow = Arrow()


def link(a: Union[Node, List[Node], Tuple[Node, ...], Group], b: Union[Node, List[Node], Tuple[Node, ...], Group], arrow: Arrow = "", style: LinkStyle = ""):
    global linksId
    linksId += 1

    if arrow == "":
        arrow = defaultArrow

    def evalList(obj):
        obj1 = ' & '.join([i._id for i in obj])
        for i in obj:
            if type(i) != Group:
                try:
                    unlinkedNodes.pop(unlinkedNodes.index(i))
                except:
                    # probably removed from another link
                    pass
        return obj1

    def evalObj(obj):
        obj1 = obj._id
        if type(obj) != Group:
            try:
                unlinkedNodes.pop(unlinkedNodes.index(obj))
            except:
                # probably removed from another link
                pass
        return obj1

    if type(a) is list or type(a) is tuple:
        obj1 = evalList(a)
    else:
        obj1 = evalObj(a)

    if type(b) is list or type(b) is tuple:
        obj2 = evalList(b)
    else:
        obj2 = evalObj(b)

    code.append(f"{obj1} {arrow._gen()} {obj2}")

    if style != "":
        code.append(f"linkStyle {linksId} {style.parameters}")


def evaluate(toFile: bool = False, clear: bool = True) -> str:
    global code
    if len(code) == 0:
        warn("The code is empty", Warning, 3)
        exit()
    # default option if orientation wasn't set by user
    if "flowchart" not in code[0]:
        code.insert(0, "flowchart TB")

    final = "```mermaid\n" + code.pop(0) + "\n"
    spacing = 4

    # build the code
    for i in code:
        if i == "end":
            spacing -= 4

        if type(i) is list:
            # if it's a node
            if i[1] not in unlinkedNodes:
                # if it's a basic node and it's linked, remove it
                if i[1].text == "" and i[1].shape == 0 and i[1].style == "":
                    # if the node isn't linked then add it to the node
                    continue
            final += ' ' * spacing + i[0] + "\n"
        else:
            final += ' ' * spacing + i + "\n"

        if i[0:8] == "subgraph":
            spacing += 4

    final += "```"

    if toFile:
        with open("output.md", "w") as f:
            f.write(final + "\n")

    # clear global variables
    if clear == True:
        global nodesId
        nodesId = -1
        groupsNames.clear()
        nodesIds.clear()
        code.clear()

    return final


def comment(comment: str) -> None:
    code.append(f"%%{comment}")


def click(node: Node, link: str):
    code.append(f'click {node._id} "{link}"')


def RGBtoHEX(r: Union[List[int], Tuple[int, ...], int], g: int = 0, b: int = 0) -> str:
    hex = "#"
    if type(r) is list or type(r) is tuple:
        rgbList = r
    else:
        rgbList = [r, g, b]

    for n in rgbList:
        obj1 = n // 16
        obj2 = n - obj1 * 16
        if obj1 >= 10:
            letters = ["a", "b", "c", "d", "e", "f"]
            obj1 = letters[obj1 - 10]
        if obj2 >= 10:
            letters = ["a", "b", "c", "d", "e", "f"]
            obj2 = letters[obj2 - 10]
        hex += f"{obj1}{obj2}"

    return hex


def set_layout(direction: int) -> None:
    assert (0 <= direction <= 3)

    if len(code) != 0:
        warn("The layout must be called at the beginning and only one time", Warning, 3)
        exit()

    directions = ["TB", "BT", "LR", "RL"]
    code.append(f"flowchart {directions[direction]}")


def set_default_arrow(arrow: Arrow) -> None:
    assert (type(arrow) == Arrow)

    global defaultArrow
    defaultArrow = arrow
