# Sistema de tracking con SQLAlchemy 2.0

Pequeno sistema de persistencia para un proyecto de Data Science: guarda
informacion sobre los `Datasets` que se procesan y los `ModelExperiment`
que se entrenan, usando el estilo declarativo moderno de SQLAlchemy 2.0
(`Mapped` / `mapped_column`), sin SQL manual.

## Archivos

- `models.py`: define `Base` y las dos entidades mapeadas, `Dataset` y
  `ModelExperiment`.
- `main.py`: crea la base de datos SQLite a partir de los modelos, e
  instancia un objeto de cada clase para confirmar que el mapeo funciona.
- `requirements.txt`: dependencias (`sqlalchemy`).

## Como ejecutar

```bash
pip install -r requirements.txt
python main.py
```

Esto genera un archivo `analytics.db` (SQLite) en el mismo directorio, con
las tablas `datasets` y `model_experiments` ya creadas segun los modelos.
El archivo `.db` no se incluye en el repositorio (esta en `.gitignore`):
se regenera solo, cada vez que se corre `main.py`.

## Que representa cada modelo

### `Dataset`

Representa un conjunto de datos que se proceso en el proyecto.

| Campo | Tipo Python | Tipo SQL generado |
|---|---|---|
| `id` | `int` (PK) | `INTEGER` |
| `name` | `str` | `VARCHAR` |
| `source_url` | `str` | `VARCHAR` |
| `num_rows` | `int` | `INTEGER` |

### `ModelExperiment`

Representa un experimento de entrenamiento de un modelo de Machine
Learning.

| Campo | Tipo Python | Tipo SQL generado |
|---|---|---|
| `id` | `int` (PK) | `INTEGER` |
| `algorithm_name` | `str` | `VARCHAR` |
| `accuracy` | `float` | `DOUBLE` |
| `is_deployed` | `bool` | `BOOLEAN` |

## Sobre el estilo declarativo 2.0

`Base` hereda de `DeclarativeBase` (no del viejo `declarative_base()`), y
cada columna se anota con `Mapped[tipo]` en vez de usar `Column(Tipo)`
explicito. SQLAlchemy deduce el tipo de columna SQL a partir de la
anotacion de tipo de Python: `Mapped[str]` se traduce a `VARCHAR`,
`Mapped[int]` a `INTEGER`, `Mapped[float]` a `DOUBLE`, `Mapped[bool]` a
`BOOLEAN`. Esto se verifico corriendo el script y consultando
`PRAGMA table_info` directamente sobre el `.db` generado.

`__tablename__` esta definido explicitamente en ambas clases: sin este
atributo, SQLAlchemy no sabe que nombre de tabla usar en SQL y tira error
al intentar mapear la clase.
