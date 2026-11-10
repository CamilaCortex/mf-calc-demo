"""calc-demo: repo de juguete para probar mi-fabrica. Desechable."""

from .ops import add, divide, mean, multiply, percent, subtract
from .parse import parse_expression

__all__ = ["add", "divide", "mean", "multiply", "parse_expression", "percent", "subtract"]
