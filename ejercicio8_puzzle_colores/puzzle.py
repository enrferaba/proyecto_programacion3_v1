"""Representación del tablero y restricciones locales/globales."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from .model import ColorConstraint, PuzzleConfig


@dataclass(slots=True)
class PaletteEntry:
    symbol: str
    name: str


class ColorPuzzle:
    """Modelo de puzzle listo para ser resuelto por backtracking."""

    def __init__(self, config: PuzzleConfig) -> None:
        self.config = config
        self.size = config.size
        self.palette = {c.symbol: PaletteEntry(symbol=c.symbol, name=c.name) for c in config.colors}
        self.colors = {c.symbol: c for c in config.colors}
        self.board: list[list[str | None]] = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.initial_counts = {symbol: 0 for symbol in self.colors}

        self._place_prefilled()
        self._validate_usage_totals()

    # ------------------------------------------------------------------
    # Construcción del estado inicial
    def _place_prefilled(self) -> None:
        for cell in self.config.prefilled:
            if cell.color not in self.colors:
                raise ValueError(f"Color desconocido en prefilled: {cell.color}")
            if not (0 <= cell.row < self.size and 0 <= cell.col < self.size):
                raise ValueError(f"Coordenadas fuera de rango: ({cell.row}, {cell.col})")
            if self.board[cell.row][cell.col] is not None:
                raise ValueError("Casilla pre-fijada duplicada")
            if self._conflicts_with_neighbors(cell.row, cell.col, cell.color):
                raise ValueError(
                    "El fichero incluye casillas precoloreadas que ya violan la restricción de adyacencia"
                )
            self.board[cell.row][cell.col] = cell.color
            self.initial_counts[cell.color] += 1

            constraint = self.colors[cell.color]
            if self.initial_counts[cell.color] > constraint.max_count:
                raise ValueError(
                    f"El color {cell.color} supera su máximo permitido solo con las casillas precoloreadas"
                )

    def _validate_usage_totals(self) -> None:
        total_cells = self.size * self.size
        min_total = sum(c.min_count for c in self.colors.values())
        max_total = sum(c.max_count for c in self.colors.values())
        if min_total > total_cells:
            raise ValueError(
                "La suma de los mínimos por color supera el número de casillas disponibles"
            )
        if max_total < total_cells:
            raise ValueError(
                "La suma de los máximos por color es insuficiente para cubrir el tablero"
            )

    # ------------------------------------------------------------------
    # Consultas auxiliares
    def remaining_cells(self, board: list[list[str | None]]) -> int:
        return sum(cell is None for row in board for cell in row)

    def _conflicts_with_neighbors(self, row: int, col: int, symbol: str) -> bool:
        for nr, nc in self._orthogonal_neighbors(row, col):
            if self.board[nr][nc] == symbol:
                return True
        return False

    def _orthogonal_neighbors(self, row: int, col: int) -> Iterable[tuple[int, int]]:
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in deltas:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.size and 0 <= nc < self.size:
                yield nr, nc

    def can_place(self, row: int, col: int, symbol: str, board: list[list[str | None]], counts: dict[str, int]) -> bool:
        if board[row][col] is not None:
            return False
        color = self.colors[symbol]
        if counts[symbol] >= color.max_count:
            return False
        for nr, nc in self._orthogonal_neighbors(row, col):
            if board[nr][nc] == symbol:
                return False
        return True

    def cell_options(self, row: int, col: int, board: list[list[str | None]], counts: dict[str, int]) -> list[ColorConstraint]:
        options: list[ColorConstraint] = []
        for color in self.colors.values():
            if self.can_place(row, col, color.symbol, board, counts):
                options.append(color)
        return options

    def all_usage_satisfied(self, counts: dict[str, int]) -> bool:
        return all(color.min_count <= counts[color.symbol] <= color.max_count for color in self.colors.values())

    def future_feasible(self, counts: dict[str, int], board: list[list[str | None]]) -> bool:
        remaining = self.remaining_cells(board)
        min_needed = 0
        max_room = 0
        for color in self.colors.values():
            used = counts[color.symbol]
            min_needed += max(0, color.min_count - used)
            max_room += max(0, color.max_count - used)
        return min_needed <= remaining <= max_room

    def describe_palette(self) -> list[str]:
        lines = []
        for color in self.colors.values():
            lines.append(color.describe())
        return lines

    def copy_board(self, board: list[list[str | None]]) -> list[list[str]]:
        return [[cell or "?" for cell in row] for row in board]

    def empty_cells(self, board: list[list[str | None]]) -> List[tuple[int, int]]:
        cells: list[tuple[int, int]] = []
        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] is None:
                    cells.append((r, c))
        return cells
