from __future__ import annotations

from pathlib import Path

import json

from ejercicio8_puzzle_colores import ColorPuzzle, PuzzleConfig
from ejercicio8_puzzle_colores.cli import load_config
from ejercicio8_puzzle_colores.solver import BacktrackingSolver


def load_demo_config() -> PuzzleConfig:
    path = Path(__file__).resolve().parent.parent / "ejercicio8_puzzle_colores" / "data" / "demo_puzzle.json"
    return load_config(path)


def test_prefilled_validation_detects_conflict(tmp_path):
    puzzle_data = {
        "size": 2,
        "colors": [
            {"name": "Rojo", "symbol": "R", "count": 2},
            {"name": "Verde", "symbol": "V", "count": 2},
        ],
        "prefilled": [
            {"row": 0, "col": 0, "color": "R"},
            {"row": 0, "col": 1, "color": "R"},
        ],
    }
    config_path = tmp_path / "conflict.json"
    config_path.write_text(json.dumps(puzzle_data), encoding="utf-8")

    config = load_config(config_path)
    try:
        ColorPuzzle(config)
    except ValueError as exc:
        assert "adyacencia" in str(exc)
    else:  # pragma: no cover - defensivo
        raise AssertionError("Se esperaba ValueError por adyacencia")


def test_solver_finds_expected_solutions():
    config = load_demo_config()
    puzzle = ColorPuzzle(config)
    solver = BacktrackingSolver(puzzle)
    solutions = solver.solve()

    # El puzzle de ejemplo produce exactamente 8 soluciones válidas
    assert len(solutions) == 8
    for board in solutions:
        flat = [cell for row in board for cell in row]
        assert flat.count("A") == 3
