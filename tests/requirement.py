from wrappers import test_this, evaluate_general
from PyMermaid.mermaid import requirement_diagram as rd


############################
##    Expected Results    ##
############################

res_test1 = """```mermaid
requirementDiagram
    requirement abc {
    }
    requirement def {
    }
    abc - contains -> def
```"""

#############################
##    Testing functions    ##
#############################

@test_this
def basic():
    # TODO
    r1 = rd.add_requirement("abc", rd.Types.requirement)
    r2 = rd.add_requirement("def", rd.Types.requirement)
    rd.add_relationship(r1, r2, rd.Relationship.contains)
    return rd.evaluate(), res_test1

@test_this
def some_values():
    # TODO
    return "", ""

@test_this
def operator_overloading():
    # TODO
    return "", ""

@test_this
def element():
    # TODO
    return "", ""

@test_this
def links():
    # TODO
    return "", ""

@test_this
def clear():
    # TODO
    return "", ""


# after all the tests, get the general info
evaluate_general()
