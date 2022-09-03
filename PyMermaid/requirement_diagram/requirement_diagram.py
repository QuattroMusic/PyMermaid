import PyMermaid.requirement_diagram._internal_requirement_diagram as _internal
from enum import Enum
from typing import Union


def add_requirement(name: str, type: 'Types', id: str = None, text: str = None, risk: 'Risk' = None, verification_method: 'VerificationMethod' = None) -> _internal.Requirement:
    return _internal.Requirement(name=name, type=type, id=id, text=text, risk=risk, verification_method=verification_method)


def add_element(name, type: str = None, doc_ref: str = None) -> _internal.Element:
    return _internal.Element(name=name, type=type, doc_ref=doc_ref)


def add_relationship(a: Union[_internal.Requirement, _internal.Element], b: Union[_internal.Requirement, _internal.Element], type: 'Relationship') -> None:
    return _internal.relationship(a=a, b=b, type=type)


def evaluate() -> str:
    return _internal.evaluate()


class Types(Enum):
    requirement = _internal.Types.requirement
    functionalRequirement = _internal.Types.functionalRequirement
    interfaceRequirement = _internal.Types.interfaceRequirement
    performanceRequirement = _internal.Types.performanceRequirement
    physicalRequirement = _internal.Types.physicalRequirement
    designConstraint = _internal.Types.designConstraint


class Risk(Enum):
    low = _internal.Risk.low
    medium = _internal.Risk.medium
    high = _internal.Risk.high


class VerificationMethod(Enum):
    analysis = _internal.VerificationMethod.analysis
    inspection = _internal.VerificationMethod.inspection
    test = _internal.VerificationMethod.test
    demonstration = _internal.VerificationMethod.demonstration


class Relationship(Enum):
    contains = _internal.Relationship.contains
    copies = _internal.Relationship.copies
    derives = _internal.Relationship.derives
    satisfies = _internal.Relationship.satisfies
    verifies = _internal.Relationship.verifies
    refines = _internal.Relationship.refines
    traces = _internal.Relationship.traces
