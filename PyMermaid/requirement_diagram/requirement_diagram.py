import PyMermaid.requirement_diagram._internal_requirement_diagram as _int
from enum import Enum
from typing import Union


def add_requirement(name: str, type: _int.Types, id: str = None, text: str = None, risk: _int.Risk = None, verification_method: _int.VerificationMethod = None) -> _int.Requirement:
    """
    TODO
    """
    return _int.Requirement(name=name, type=type, id=id, text=text, risk=risk, verification_method=verification_method)


def add_element(name, type: str = None, doc_ref: str = None) -> _int.Element:
    """
    TODO
    """
    return _int.Element(name=name, type=type, doc_ref=doc_ref)


def add_relationship(a: _int.Requirement | _int.Element, b: _int.Requirement | _int.Element, type: _int.Relationship) -> None:
    """
    TODO
    """
    return _int.relationship(a=a, b=b, type=type)


def evaluate() -> str:
    """
    TODO
    """
    return _int.evaluate()


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
