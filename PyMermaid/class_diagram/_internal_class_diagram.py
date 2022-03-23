#imports

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

        code.append(f"{types[visibility]}{var}{classifiers[classifier]}")

    def add_method(self,function: str,visibility:int = 0,classifier:int = 0):
        self._times += 1
        types = ["", "+", "-", "#", "~"]
        classifiers = ["", "$","*"]

        code.append(f"{types[visibility]}{function}(){classifiers[classifier]}")
