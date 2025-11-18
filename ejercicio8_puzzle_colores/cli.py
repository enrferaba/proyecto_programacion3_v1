"""Interfaz de línea de comandos para el puzzle de colores."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .model import PuzzleConfig
from .puzzle import ColorPuzzle
from .render import format_board, format_summary
from .solver import BacktrackingSolver


def load_config(path: Path) -> PuzzleConfig:
    with path.open("r", encoding="utf-8") as fh:
        data: Any = json.load(fh)
    return PuzzleConfig.from_dict(data)


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Resuelve el puzzle de colores descrito en el PDF (Opción 1) "
            "empleando backtracking."
        )
    )
    parser.add_argument(
        "config",
        type=Path,
        help=(
            "Ruta al archivo JSON que describe el tablero, la paleta "
            "de colores y las restricciones globales."
        ),
    )
    parser.add_argument(
        "--max-solutions",
        type=int,
        default=None,
        help=(
            "Máximo de soluciones a mostrar. Por defecto se muestran todas, "
            "pero puede limitarse para tableros grandes."
        ),
    )
    return parser


def run_cli(args: list[str] | None = None) -> int:
    parser = build_argument_parser()
    parsed = parser.parse_args(args=args)

    config = load_config(parsed.config)
    puzzle = ColorPuzzle(config)

    print(format_summary(puzzle))
    print("\nTablero inicial:\n")
    print(format_board(puzzle.board, puzzle.palette))

    solver = BacktrackingSolver(puzzle, max_solutions=parsed.max_solutions)
    solutions = solver.solve()

    if not solutions:
        print("\nNo se encontraron soluciones para los datos proporcionados.")
        return 1

    print(f"\nSe encontraron {len(solutions)} solucion(es).\n")
    for idx, board in enumerate(solutions, start=1):
        print(f"Solución #{idx}:")
        print(format_board(board, puzzle.palette))
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(run_cli())
