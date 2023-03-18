import PyMermaid.internals.requirement_diagram as _int
from enum import Enum


def add_requirement(name: str, type: _int.Types = _int.Types.requirement, id: str = None, text: str = None, risk: _int.Risk = None, verification_method: _int.VerificationMethod = None) -> _int.Requirement:
    """
    TODO
    """
    return _int.Requirement(name=name, type=type, id=id, text=text, risk=risk, verification_method=verification_method)

def add_element(name: str, type: str = None, doc_ref: str = None) -> _int.Element:
    """
    TODO
    """
    return _int.Element(name=name, type=type, doc_ref=doc_ref)

def add_relationship(from_: _int.Requirement | _int.Element, to_: _int.Requirement | _int.Element, type: _int.Relationship) -> None:
    """
    TODO
    """
    return _int.relationship(from_=from_, to_=to_, type=type)

def evaluate() -> str:
    """
    TODO
    """
    return _int.evaluate()

def clear() -> None:
    """
    TODO
    """
    return _int.clear()

class Types(Enum):
    requirement             = _int.Types.requirement.value
    functionalRequirement   = _int.Types.functionalRequirement.value
    interfaceRequirement    = _int.Types.interfaceRequirement.value
    performanceRequirement  = _int.Types.performanceRequirement.value
    physicalRequirement     = _int.Types.physicalRequirement.value
    designConstraint        = _int.Types.designConstraint.value

class Risk(Enum):
    low     = _int.Risk.low.value
    medium  = _int.Risk.medium.value
    high    = _int.Risk.high.value

class VerificationMethod(Enum):
    analysis       = _int.VerificationMethod.analysis.value
    inspection     = _int.VerificationMethod.inspection.value
    test           = _int.VerificationMethod.test.value
    demonstration  = _int.VerificationMethod.demonstration.value

class Relationship(Enum):
    contains   = _int.Relationship.contains.value
    copies     = _int.Relationship.copies.value
    derives    = _int.Relationship.derives.value
    satisfies  = _int.Relationship.satisfies.value
    verifies   = _int.Relationship.verifies.value
    refines    = _int.Relationship.refines.value
    traces     = _int.Relationship.traces.value
