import wrappers as wrap
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


#############################
##    Testing functions    ##
#############################

@wrap.test_it
def test1():
    f.clear()
    n1 = f.add_node("Test1")
    n2 = f.add_node("Test2")

    f.link(n1, n2)

    return f.evaluate(), res_test1


# after all the tests, get the general info
wrap.evaluate_general()
