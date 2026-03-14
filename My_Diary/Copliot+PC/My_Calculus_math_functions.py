import functools, math

@functools.cache
def xyrt(number: float, x: float, y: float) -> float:
    xyrt: float = number ** (x / y)
    return xyrt

@functools.cache
def cotan(number: float) -> float:
    cotangent: float = 1 / math.tan(number)
    return cotangent

@functools.cache
def acotan(number: float) -> float:
    acotangent: float = 1 / math.atan(number)
    return acotangent

@functools.cache
def cotanh(number: float) -> float:
    cotangenthyper: float = 1 / math.tanh(number)
    return cotangenthyper

@functools.cache
def acotanh(number: float) -> float:
    acotangenthyper: float = 1 / math.atanh(number)
    return acotangenthyper
