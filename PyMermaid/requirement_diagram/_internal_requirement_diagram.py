from enum import Enum
from typing import Union, List

code: List[Union['Requirement', 'Element', str]] = []


class Types(Enum):
    requirement = object()
    functionalRequirement = object()
    interfaceRequirement = object()
    performanceRequirement = object()
    physicalRequirement = object()
    designConstraint = object()


class Risk(Enum):
    low = object()
    medium = object()
    high = object()


class VerificationMethod(Enum):
    analysis = object()
    inspection = object()
    test = object()
    demonstration = object()


class Relationship(Enum):
    contains = object()
    copies = object()
    derives = object()
    satisfies = object()
    verifies = object()
    refines = object()
    traces = object()


class Requirement:
    def __init__(self, name: str, type: Types, id: str = None, text: str = None, risk: Risk = None, verification_method: VerificationMethod = None):
        self.name = name
        self.type = type
        self.id = id
        self.text = text
        self.risk = risk
        self.verification_method = verification_method

        # adding it to the code
        code.append(self)


class Element:
    def __init__(self, name, type: str = None, doc_ref: str = None):
        self.name = name
        self.type = type
        self.doc_ref = doc_ref

        code.append(self)


def relationship(a: Union[Requirement, Element], b: Union[Requirement, Element], type: Relationship):
    code.append(f"{a.name} - {type.name} -> {b.name}")


def evaluate():
    final = ["```mermaid", "requirementDiagram"]

    for item in code:
        if type(item) == Requirement:
            attributes = [''.join(i) for i in [(' ' * 8 + "id: ", item.id), (' ' * 8 + "text: ", item.text), (' ' * 8 + "risk: ", item.risk.name), (' ' * 8 + "verifymethod: ", item.verification_method.name)] if i[1] is not None]
            final += [f"    {item.type.name} {item.name} {{", "\n".join(attributes), "    }"]
        elif type(item) == Element:
            attributes = [''.join(i) for i in [(' ' * 8 + "type: \"", item.type, "\""), (' ' * 8 + "docRef: ", item.doc_ref)] if i[1] is not None]
            final += [f"    element {item.name} {{", "\n".join(attributes), "    }"]

    # add links at the end
    for item in code:
        if type(item) == str:
            final.append(' ' * 4 + item)

    return '\n'.join(final + ["```"])
