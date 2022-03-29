from typing import List

states_created: List["State"] = []

code: List[str] = []

# state object used by state diagrams
class State:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self):
        return self.name

def link_from_start(state: State):
    code.append(f"[*] --> {state.get_name()}")

def link_to_end(state: State):
    code.append(f"{state.get_name()} --> [*]")

def evaluate() -> str:
    output = "stateDiagram-v2\n"
    indent_level = 1
    for line in code:
        if "state" in line: indent_level += 1
        if "}" in line:     indent_level -= 1
        
        output += " " * (indent_level * 4) + f"{line}\n"
    
    return output

if __name__ == "__main__":
    node = State("Test")
    link_from_start(node)
    link_to_end(node)
    print(evaluate())