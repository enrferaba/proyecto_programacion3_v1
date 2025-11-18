"""Solución al puzzle de colores (Opción 1)."""

from .model import ColorConstraint, PuzzleConfig, PreFilledCell
from .puzzle import ColorPuzzle
from .solver import BacktrackingSolver
from .cli import run_cli

__all__ = [
    "ColorConstraint",
    "PreFilledCell",
    "PuzzleConfig",
    "ColorPuzzle",
    "BacktrackingSolver",
    "run_cli",
]
