#imports
from typing import Union,List,Tuple
from enum import Enum

#costants
class Visibility(Enum):
    NONE = 0
    PUBLIC = 1
    PRIVATE = 2
    PROTECTED = 3
    PACKAGE_INTERNAL = 4

class FieldClassifier(Enum):
    NONE = 0
    STATIC = 1

class MethodClassifier(Enum):
    NONE = 0
    STATIC = 1
    ABSTRACT = 2


#variables

#code
code = ["classDiagram"]
identation_level = 0

class Class:
    def __init__(self, name: str):
        name = name.replace("<", "~").replace(">", "~")
        self.name = name
        code.append(f"class {self.name}")

    def add_field(self, name: str, field_type: str, visibility: Visibility = Visibility.NONE, classifier: FieldClassifier = FieldClassifier.NONE):
        types = ["", "+","-","#","~"]
        classifiers = ["", "$"]
        field_type = field_type.replace("<","~").replace(">","~")
        
        code.append(f"{self.name} : {types[visibility.value]}{field_type} {name}{classifiers[classifier.value]}")

    def add_method(self, name: str, method_input_types: List[Tuple[str, str]], method_return_type: str = "", visibility: Visibility = Visibility.NONE, classifier: MethodClassifier = MethodClassifier.NONE):
        types = ["", "+","-","#","~"]
        classifiers = ["", "$", "*"]
        return_type = method_return_type.replace("<","~").replace(">","~")
        input_types = [f"{input_type.replace('<','~').replace('>','~')}{' ' if len(input_type) > 0 else ''}{input_name}" for input_type, input_name in method_input_types]
        
        code.append(f"{self.name} : {types[visibility.value]}{return_type}{' ' if len(return_type) > 0 else ''}{name}({', '.join(input_types)}){classifiers[classifier.value]}")
    
def link(a,b):
    ...

def evaluate():
    return "\n".join(code)

if __name__ == "__main__":
    c = Class("Square<Shape>")
    c.add_field("id", "int")
    c.add_field("position", "List<int>")
    c.add_method("setPoints", [("List<int>","points")])
    c.add_method("getPoints", [("","")], "List<int>")
    print(evaluate())