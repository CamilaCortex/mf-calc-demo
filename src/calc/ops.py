"""Operaciones aritméticas básicas."""

from __future__ import annotations

from collections.abc import Iterable


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("no se puede dividir entre cero")
    return a / b


def mean(values: Iterable[float]) -> float:
    vals = list(values)
    if not vals:
        raise ValueError("mean() necesita al menos un valor")
    return sum(vals) / len(vals)


def percent(part: float, whole: float) -> float:
    """Qué porcentaje es ``part`` de ``whole`` (0-100)."""
    return divide(part, whole) * 10
