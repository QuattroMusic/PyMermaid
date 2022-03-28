#imports
from typing import Union,List,Tuple

#costants
visibility_public = 1
visibility_private = 2
visibility_protected = 3
visibility_packageInternal = 4
classifier_static = 1
classifier_abstract = 2

#variables

#code
code = []

class Class:
    def __init__(self,name):

        name = name.replace("<", "~").replace(">", "~")

        self.name = name
        self._times = 0

        code.append(f"class {self.name}")

    def __enter__(self):
        #if created using the with, add the { symbol
        code[-1] += "{"
        return self

    def __exit__(self, *args):
        code.append("}")
        if self._times == 0:
            for i in range(2):
                code.pop(-1)
            code.append(f"class {self.name}")

    def add_field(self,var: str, visibility: int = 0,classifier:int = 0):
        self._times += 1

        types = ["","+","-","#","~"]
        classifiers = ["", "$"]
        var = var.replace("<","~").replace(">","~")

        code.append(f"{types[visibility]} {var}{classifiers[classifier]}")

    def add_method(self,function: str,visibility:int = 0,classifier:int = 0,arguments: Union[str,List[str],Tuple[str,...]] = "",returns: Union[str,List[str],Tuple[str,...]] = ""):
        self._times += 1
        types = ["", "+", "-", "#", "~"]
        classifiers = ["", "$","*"]
        if type(arguments) is tuple or type(arguments) is list:
            arguments = ", ".join(arguments)
        arguments = arguments.replace("<","~").replace(">","~")

        if type(returns) is tuple or type(returns) is list:
            returns = ", ".join(returns)
        returns = returns.replace("<","~").replace(">","~")

        code.append(f"{types[visibility]}{function}({arguments}){classifiers[classifier]} :{returns}")

def link(a,b):
    ...

def evaluate():
    return "\n".join(code)
