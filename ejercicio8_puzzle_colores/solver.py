"""Algoritmo de backtracking para el puzzle de colores."""
from __future__ import annotations

from copy import deepcopy
from typing import Sequence

from .puzzle import ColorPuzzle


class BacktrackingSolver:
    def __init__(self, puzzle: ColorPuzzle, max_solutions: int | None = None) -> None:
        self.puzzle = puzzle
        self.max_solutions = max_solutions
        self.solutions: list[list[list[str]]] = []

    def solve(self) -> list[list[list[str]]]:
        board = deepcopy(self.puzzle.board)
        counts = dict(self.puzzle.initial_counts)
        self._backtrack(board, counts)
        return self.solutions

    # ------------------------------------------------------------------
    def _select_cell(self, board: list[list[str | None]], counts: dict[str, int]) -> tuple[int, int, Sequence[str]] | None:
        best_cell: tuple[int, int] | None = None
        best_options: list[str] | None = None
        for row in range(self.puzzle.size):
            for col in range(self.puzzle.size):
                if board[row][col] is not None:
                    continue
                options = [color.symbol for color in self.puzzle.cell_options(row, col, board, counts)]
                if not options:
                    return (row, col, [])
                if best_options is None or len(options) < len(best_options):
                    best_cell = (row, col)
                    best_options = options
                    if len(best_options) == 1:
                        return (row, col, options)
        if best_cell is None or best_options is None:
            return None
        return (*best_cell, best_options)

    def _backtrack(self, board: list[list[str | None]], counts: dict[str, int]) -> None:
        if self.max_solutions is not None and len(self.solutions) >= self.max_solutions:
            return

        selection = self._select_cell(board, counts)
        if selection is None:
            if self.puzzle.all_usage_satisfied(counts):
                self.solutions.append(deepcopy(self.puzzle.copy_board(board)))
            return

        row, col, options = selection
        if not options:
            return

        for symbol in options:
            board[row][col] = symbol
            counts[symbol] += 1

            if self.puzzle.future_feasible(counts, board):
                self._backtrack(board, counts)

            counts[symbol] -= 1
            board[row][col] = None
