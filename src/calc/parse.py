"""Evalúa expresiones simples ``"<num> <op> <num>"``, p. ej. ``"3 + 4"``."""

from __future__ import annotations

from .ops import add, divide, multiply, subtract

OPS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def parse_expression(text: str) -> float:
    parts = text.split()
    if len(parts) != 3:
        raise ValueError(f"expresión inválida: {text!r}")
    left, op, right = parts
    if op not in OPS:
        raise ValueError(f"operador desconocido: {op!r}")
    return OPS[op](float(left), float(right))
