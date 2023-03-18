from wrappers import test_this, evaluate_general

from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.dirname(os_path.dirname(os_path.abspath(__file__))))

import PyMermaid.flowchart as f


############################
##    Expected Results    ##
############################

res_basic = """```mermaid
flowchart TB
    0["Test1"]
    1["Test2"]
    0 --> 1
    2["A"]
    3["B"]
    4["C"]
    2 --> 3 & 4
```"""
res_all_the_shapes = """```mermaid
flowchart TB
    0["A"]
    1("B")
    2(["C"])
    3[["D"]]
    4[("E")]
    5(("F"))
    6>"G"]
    7{"H"}
    8{{"I"}}
    9[/"J"/]
    10[\\"K"\\]
    11[/"L"\\]
    12[\\"M"/]
    13((("N")))
```"""
res_operator_overloading = """```mermaid
flowchart TB
    0["A"]
    1["B"]
    0 --> 1
```"""
res_grouping = """```mermaid
flowchart TB
    subgraph 0["G1"]
        direction TB
        1["A"]
        2["B"]
        1 --> 2
    end
    3["C"]
    3 --> 0
```"""
res_arrows = """```mermaid
flowchart TB
```"""
res_node_styling = """```mermaid
flowchart TB
```"""
res_link_styling = """```mermaid
flowchart TB
```"""
res_clear = """```mermaid
flowchart TB
```"""
res_layout = """```mermaid
flowchart TB
```"""

#############################
##    Testing functions    ##
#############################

@test_this
def basic():
    f.clear()
    n1 = f.add_node("Test1")
    n2 = f.add_node("Test2")

    f.link(n1, n2)
    n3 = f.add_node("A")
    n4 = f.add_node("B")
    n5 = f.add_node("C")
    f.link(n3, [n4, n5])

    return f.evaluate(), res_basic

@test_this
def all_the_shapes():
    f.clear()
    f.add_node("A", shape=f.NodeShapes.default)
    f.add_node("B", shape=f.NodeShapes.round_edges)
    f.add_node("C", shape=f.NodeShapes.stadium)
    f.add_node("D", shape=f.NodeShapes.subroutine)
    f.add_node("E", shape=f.NodeShapes.cylindrical)
    f.add_node("F", shape=f.NodeShapes.circle)
    f.add_node("G", shape=f.NodeShapes.asymmetric)
    f.add_node("H", shape=f.NodeShapes.rhombus)
    f.add_node("I", shape=f.NodeShapes.hexagon)
    f.add_node("J", shape=f.NodeShapes.parallelogram)
    f.add_node("K", shape=f.NodeShapes.parallelogram_alt)
    f.add_node("L", shape=f.NodeShapes.trapezoid)
    f.add_node("M", shape=f.NodeShapes.trapezoid_alt)
    f.add_node("N", shape=f.NodeShapes.double_circle)

    return f.evaluate(), res_all_the_shapes

@test_this
def grouping():
    f.clear()
    with f.add_group("G1") as group:
        n1 = f.add_node("A")
        n2 = f.add_node("B")
        f.link(n1, n2)
    n3 = f.add_node("C")
    f.link(n3, group)
    
    return f.evaluate(), res_grouping

@test_this
def operator_overloading():
    f.clear()
    f.add_node("A") >> f.add_node("B")
    
    return f.evaluate(), res_operator_overloading

@test_this
def arrows():
    f.clear()
    return f.evaluate(), res_arrows

@test_this
def node_styling():
    f.clear()
    return f.evaluate(), res_node_styling

@test_this
def link_styling():
    f.clear()
    return f.evaluate(), res_link_styling

@test_this
def clear():
    f.clear()
    return f.evaluate(), res_clear

@test_this
def layout():
    f.clear()
    return f.evaluate(), res_layout


# after all the tests, get the general info
evaluate_general()
