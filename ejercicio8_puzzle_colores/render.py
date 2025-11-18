"""Funciones auxiliares para mostrar el tablero."""
from __future__ import annotations

from typing import Mapping

from .puzzle import ColorPuzzle

ANSI_CODES: Mapping[str, str] = {
    "negro": "30",
    "rojo": "31",
    "verde": "32",
    "amarillo": "33",
    "azul": "34",
    "magenta": "35",
    "cian": "36",
    "blanco": "37",
}


def colorize(symbol: str, color_name: str) -> str:
    lower = color_name.lower()
    code = ANSI_CODES.get(lower)
    if code is None:
        return symbol
    return f"\033[{code}m{symbol}\033[0m"


def format_board(board: list[list[str | None]], palette: Mapping[str, object]) -> str:
    size = len(board)
    horizontal = "+" + "+".join(["---"] * size) + "+"
    lines = [horizontal]
    for row in board:
        rendered_row = "|"
        for cell in row:
            if cell is None:
                rendered_row += "   |"
            else:
                name = getattr(palette[cell], "name", cell)
                rendered_row += f" {colorize(cell, name)} |"
        lines.append(rendered_row)
        lines.append(horizontal)
    return "\n".join(lines)


def format_summary(puzzle: ColorPuzzle) -> str:
    lines = [
        "Puzzle de Colores",
        f"- Tamaño del tablero: {puzzle.size}x{puzzle.size}",
        "- Paleta y restricciones:",
    ]
    for desc in puzzle.describe_palette():
        lines.append(f"  • {desc}")
    if puzzle.config.prefilled:
        lines.append("- Casillas fijadas:")
        for cell in puzzle.config.prefilled:
            lines.append(f"  • ({cell.row}, {cell.col}) = {cell.color}")
    else:
        lines.append("- Casillas fijadas: ninguna")
    return "\n".join(lines)
