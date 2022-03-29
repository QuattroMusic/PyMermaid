from typing import List, Union

code: List[str] = []
nodes_created: List["State"] = []

# state object used by state diagrams
class State:
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
        nodes_created.append(self)
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

def link_from_start(state: Union[State, str]):
    if isinstance(state, State):
        code.append(f"[*] --> {state.get_name()}")
    elif isinstance(state, str):
        code.append(f"[*] --> {state}")
    else:
        raise TypeError("Input type must be str or Union")

def link_to_end(state: Union[State, str]):
    if isinstance(state, State):
        code.append(f"{state.get_name()} --> [*]")
    elif isinstance(state, str):
        code.append(f"{state} --> [*]")
    else:
        raise TypeError("Input type must be str or Union")

def link(stateFrom: Union[State, str], stateTo: Union[State, str], text: str = None):
    if not isinstance(stateFrom, State) and not isinstance(stateFrom, str):
        raise TypeError("stateFrom type must be str or Union")
    if not isinstance(stateTo, State) and not isinstance(stateFrom, str):
        raise TypeError("stateTo type must be str or Union")
    
    extra = f": {text}" if text else ""
    from_name = stateFrom.get_name() if isinstance(stateFrom, State) else stateFrom
    to_name   = stateTo.get_name()   if isinstance(stateTo, State)   else stateTo
    code.append(f"{from_name} --> {to_name}{extra}")

def evaluate() -> str:
    output = "stateDiagram-v2\n"
    indent_level = 1
    
    # setup all nodes with descriptions
    for node in nodes_created:
        if node.description:
            output += " " * (indent_level * 4) + f"state \"{node.get_description()}\" as {node.get_name()}\n"
    
    # create whole document
    for line in code:
        if "{" in line: indent_level += 1
        if "}" in line: indent_level -= 1
        
        output += " " * (indent_level * 4) + f"{line}\n"
    
    return output

if __name__ == "__main__":
    n1 = State("Test", "This is a test description")
    n2 = State("Second", "Second description")
    link_from_start(n1)
    link_from_start("Prova")
    link("Prova", n2)
    link(n1, n2, "This is a transition")
    link_to_end(n2)
    print(evaluate())