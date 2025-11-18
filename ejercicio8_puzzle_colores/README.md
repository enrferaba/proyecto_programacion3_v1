# Ejercicio 8 · Puzzle de Colores (Opción 1)

Esta carpeta contiene una implementación completa del **Puzzle de Colores**
descrito en la opción 1 (máx. 8) del documento PDF compartido. El enfoque
sigue el estilo del ejercicio de referencia del profesor: se definen clases
para los objetos principales del problema (paleta de colores, tablero y
restricciones) y se resuelve mediante un algoritmo de **backtracking** que
explora todas las soluciones posibles.

## Estructura

```
ejercicio8_puzzle_colores/
├── __init__.py
├── cli.py              # Punto de entrada por CLI
├── model.py            # Definición de los datos y validaciones básicas
├── puzzle.py           # Lógica del tablero y restricciones
├── render.py           # Utilidades para mostrar el tablero y la paleta
├── solver.py           # Implementación del backtracking
├── data/
│   └── demo_puzzle.json  # Ejemplo listo para ejecutar
└── README.md
```

Los tests unitarios se encuentran en `tests/test_color_puzzle.py`.

## Uso rápido

1. Activa el entorno (si aplica) y sitúate en la raíz del repositorio.
2. Ejecuta:

```bash
python -m ejercicio8_puzzle_colores.cli ejercicio8_puzzle_colores/data/demo_puzzle.json
```

3. El programa mostrará un resumen del puzzle, el tablero inicial y todas las
soluciones encontradas. Con `--max-solutions N` se puede limitar el número de
soluciones impresas si el espacio de búsqueda es grande.

## Formato del archivo JSON

```json
{
  "size": 3,
  "colors": [
    {"name": "Azul", "symbol": "A", "count": 3},
    {"name": "Rojo", "symbol": "R", "min": 2, "max": 4},
    {"name": "Verde", "symbol": "V", "min": 2, "max": 4}
  ],
  "prefilled": [
    {"row": 0, "col": 0, "color": "A"},
    {"row": 2, "col": 2, "color": "A"}
  ]
}
```

- `size`: tamaño `N` del tablero (`N x N`).
- `colors`: restricciones por color. Cada color define un símbolo (o se
  toma la inicial del nombre). Se admite:
  - `count`: número fijo de apariciones.
  - o bien `min` y `max`: intervalo permitido de apariciones.
- `prefilled`: casillas ya coloreadas (no se pueden modificar).

## Características clave

- Validaciones exhaustivas de entrada (coordenadas, colores, solapamientos y
  coherencia de las restricciones globales).
- Selección heurística de la siguiente casilla a expandir (MRV) para acelerar
  el backtracking.
- Comprobaciones de poda que aseguran el respeto de los mínimos/máximos globales
  antes de profundizar en el árbol de búsqueda.
- Representación visual amigable del tablero (utiliza colores ANSI cuando es
  posible) y resumen textual de la paleta.

## Tests

Ejecuta los tests con:

```bash
pytest
```

El caso de prueba incluido valida tanto la creación del puzzle como la
búsqueda de soluciones para el `demo_puzzle`.
