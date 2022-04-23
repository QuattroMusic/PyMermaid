from typing import List, Union

code: List[str] = []
nodes_created: List["State"] = []


def link_from_start(state: Union["State", str]):
    if isinstance(state, State):
        code.append(f"[*] --> {state.get_name()}")
    elif isinstance(state, str):
        code.append(f"[*] --> {state}")
    else:
        raise TypeError("Input type must be str or Union")

def link_to_end(state: Union["State", str]):
    if isinstance(state, State):
        code.append(f"{state.get_name()} --> [*]")
    elif isinstance(state, str):
        code.append(f"{state} --> [*]")
    else:
        raise TypeError("Input type must be str or Union")

def link(stateFrom: Union["State", str], stateTo: Union["State", str], text: str = None):
    if not isinstance(stateFrom, State) and not isinstance(stateFrom, str):
        raise TypeError("stateFrom type must be str or Union")
    if not isinstance(stateTo, State) and not isinstance(stateFrom, str):
        raise TypeError("stateTo type must be str or Union")
    
    extra = f": {text}" if text else ""
    from_name = stateFrom.get_name() if isinstance(stateFrom, State) else stateFrom
    to_name   = stateTo.get_name()   if isinstance(stateTo, State)   else stateTo
    code.append(f"{from_name} --> {to_name}{extra}")

# state object used by state diagrams
class State:
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
        self._canBeCalled = False
        nodes_created.append(self)
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def __enter__(self):
        self._canBeCalled = True
        code.append("state " + self.get_name() + " {")
        return self
    
    def __exit__(self, *args, **kwargs):
        self._canBeCalled = False
        code.append("}")

    def link_from_start(self, state: Union["State", str]):
        if self._canBeCalled:
            link_from_start(state)
    
    def link_to_end(self, state: Union["State", str]):
        if self._canBeCalled:
            link_to_end(state)
    
    def link(self, stateFrom: Union["State", str], stateTo: Union["State", str], text: str = None):
        if self._canBeCalled:
            link(stateFrom, stateTo, text)
    
def evaluate() -> str:
    output = "stateDiagram-v2\n"
    indent_level = 1
    
    # setup all nodes with descriptions
    for node in nodes_created:
        if node.description:
            output += " " * (indent_level * 4) + f"state \"{node.get_description()}\" as {node.get_name()}\n"
    
    # create whole document
    for line in code:
        if "}" in line: indent_level -= 1
        
        output += " " * (indent_level * 4) + f"{line}\n"
        
        if "{" in line: indent_level += 1
    
    return output
