from enum import Enum


class Types(Enum):
    requirement = "requirement"
    functionalRequirement = "functionalRequirement"
    interfaceRequirement = "interfaceRequirement"
    performanceRequirement = "performanceRequirement"
    physicalRequirement = "physicalRequirement"
    designConstraint = "designConstraint"


class Risk(Enum):
    low = "Low"
    medium = "Medium"
    high = "High"


class VerificationMethod(Enum):
    analysis = "Analysis"
    inspection = "Inspection"
    test = "Test"
    demonstration = "Demonstration"


class Relationship(Enum):
    contains = "contains"
    copies = "copies"
    derives = "derives"
    satisfies = "satisfies"
    verifies = "verifies"
    refines = "refines"
    traces = "traces"

code = []


class Requirement:
    def __init__(self, name: str, type: Types = Types.requirement, id: str = None, text: str = None, risk: Risk = None, verification_method: VerificationMethod = None):
        self.name = name
        self.type = type.value
        self.id = id
        self.text = text
        self.risk = risk
        self.verification_method = verification_method

        code.append(self)


class Element:
    def __init__(self, name: str, type: str = None, doc_ref: str = None):
        self.name = name
        self.type = type
        self.doc_ref = doc_ref

        code.append(self)


def relationship(a: Requirement | Element, b: Requirement | Element, type: Relationship):
    code.append(f"{a.name} - {type.value} -> {b.name}")


def get_requirement(item: Requirement) -> str:
    args = ""
    # add the spacing, since you cannot put requirements one inside another, the spacing is always 8
    if item.id is not None:
        args += f"        id: {item.id}\n"
    if item.text is not None:
        args += f"        text: {item.text}\n"
    if item.risk is not None:
        args += f"        risk: {item.risk.value}\n"
    if item.verification_method is not None:
        args += f"        verifymethod: {item.verification_method.value}\n"
    
    return f"    {item.type} {item.name} {{\n" + args + "    }\n"


def get_element(item: Element) -> str:
    args = ""
    # add the spacing, since you cannot put requirements one inside another, the spacing is always 8
    if item.type is not None:
        args += f"        type: {item.type}\n"
    if item.doc_ref is not None:
        args += f"        docRef: {item.doc_ref}\n"
    
    return f"    element {item.name} {{\n" + args + "    }\n"


def evaluate():
    final = "```mermaid\nrequirementDiagram\n\n"

    for item in code:
        if type(item) == Requirement:
            final += get_requirement(item)
        elif type(item) == Element:
            final += get_element(item)
        elif type(item) == str:
            # if it's a link
            final += '    ' + item + "\n"

    return final + "```"
