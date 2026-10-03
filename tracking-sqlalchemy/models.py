"""
Definicion de las entidades del sistema de tracking, usando el estilo
declarativo de SQLAlchemy 2.0 (Mapped / mapped_column), sin mezclar con
el estilo antiguo basado en Column().
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Clase base de la que heredan todos los modelos mapeados."""
    pass


class Dataset(Base):
    """Representa un conjunto de datos procesado en el proyecto."""

    __tablename__ = "datasets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    source_url: Mapped[str]
    num_rows: Mapped[int]

    def __repr__(self) -> str:
        return f"Dataset(id={self.id!r}, name={self.name!r}, num_rows={self.num_rows!r})"


class ModelExperiment(Base):
    """Representa un experimento de entrenamiento de un modelo de ML."""

    __tablename__ = "model_experiments"

    id: Mapped[int] = mapped_column(primary_key=True)
    algorithm_name: Mapped[str]
    accuracy: Mapped[float]
    is_deployed: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return (
            f"ModelExperiment(id={self.id!r}, algorithm_name={self.algorithm_name!r}, "
            f"accuracy={self.accuracy!r}, is_deployed={self.is_deployed!r})"
        )
