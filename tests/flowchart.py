from wrappers import test_this, evaluate_general
from PyMermaid.mermaid import flowchart as f


############################
##    Expected Results    ##
############################

res_test1 = """```mermaid
flowchart TB
    0["Test1"]
    1["Test2"]
    0 --> 1
```"""
res_test2 = """```mermaid
flowchart TB
    0[("A")]
    1("B")
    2[\\"C"/]
    0 --> 1 & 2
```"""


#############################
##    Testing functions    ##
#############################

@test_this
def basic_flowchart():
    f.clear()
    n1 = f.add_node("Test1")
    n2 = f.add_node("Test2")

    f.link(n1, n2)

    return f.evaluate(), res_test1

@test_this
def node_with_shapes():
    f.clear()
    n1 = f.add_node("A", shape=f.NodeShapes.cylindrical)
    n2 = f.add_node("B", shape=f.NodeShapes.round_edges)
    n3 = f.add_node("C", shape=f.NodeShapes.trapezoid_alt)

    f.link(n1, [n2, n3])

    return f.evaluate(), res_test2

@test_this
def operator_overloading():
    # TODO
    return "", ""

@test_this
def grouping():
    # TODO
    return "", ""

@test_this
def arrows():
    # TODO
    return "", ""

@test_this
def node_styling():
    # TODO
    return "", ""

@test_this
def link_styling():
    # TODO
    return "", ""

@test_this
def clear():
    # TODO
    return "", ""

@test_this
def layout():
    # TODO
    return "", ""


# after all the tests, get the general info
evaluate_general()
