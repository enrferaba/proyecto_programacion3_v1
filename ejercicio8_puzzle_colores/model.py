"""Modelos de datos y validaciones básicas."""
from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class ColorConstraint:
    """Restricción global asociada a un color."""

    name: str
    symbol: str
    min_count: int
    max_count: int

    DEFAULT_SYMBOLS: ClassVar[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # fallback

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "ColorConstraint":
        name = str(data["name"]).strip()
        symbol = str(data.get("symbol") or name[0].upper())
        symbol = symbol.strip() or name[0].upper()

        if "count" in data:
            count = int(data["count"])
            min_count = max_count = count
        else:
            try:
                min_count = int(data["min"])
                max_count = int(data["max"])
            except KeyError as exc:  # pragma: no cover - defensivo
                raise ValueError(
                    "Debe indicarse 'count' o ('min' y 'max') para cada color"
                ) from exc

        if min_count < 0 or max_count < 0:
            raise ValueError("Los contadores deben ser no negativos")
        if min_count > max_count:
            raise ValueError("Se requiere min_count <= max_count")

        return cls(name=name, symbol=symbol, min_count=min_count, max_count=max_count)

    @property
    def interval(self) -> tuple[int, int]:
        return (self.min_count, self.max_count)

    def describe(self) -> str:
        if self.min_count == self.max_count:
            return f"{self.name} ({self.symbol}): {self.min_count} apariciones exactas"
        return (
            f"{self.name} ({self.symbol}): entre {self.min_count} y "
            f"{self.max_count} apariciones"
        )


@dataclass(frozen=True)
class PreFilledCell:
    row: int
    col: int
    color: str

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "PreFilledCell":
        return cls(row=int(data["row"]), col=int(data["col"]), color=str(data["color"]))


@dataclass(frozen=True)
class PuzzleConfig:
    size: int
    colors: list[ColorConstraint]
    prefilled: list[PreFilledCell]

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "PuzzleConfig":
        size = int(data["size"])
        if size <= 0:
            raise ValueError("El tamaño del tablero debe ser positivo")

        colors_data = data.get("colors")
        if not isinstance(colors_data, list) or not colors_data:
            raise ValueError("Debe especificarse una lista de colores")
        colors = [ColorConstraint.from_dict(item) for item in colors_data]

        prefilled_data = data.get("prefilled", [])
        if not isinstance(prefilled_data, list):
            raise ValueError("'prefilled' debe ser una lista de casillas")
        prefilled = [PreFilledCell.from_dict(item) for item in prefilled_data]

        return cls(size=size, colors=colors, prefilled=prefilled)
