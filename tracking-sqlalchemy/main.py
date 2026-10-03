"""
Script de inicializacion: crea las tablas en SQLite a partir de los
modelos declarativos, e instancia un objeto de cada clase para
confirmar que el mapeo funciona.
"""

from sqlalchemy import create_engine

from models import Base, Dataset, ModelExperiment

engine = create_engine("sqlite:///analytics.db")

# Genera analytics.db con las tablas 'datasets' y 'model_experiments',
# segun lo definido en models.py. Si el archivo ya existe, create_all
# no vuelve a crear las tablas que ya estan (no falla por eso).
Base.metadata.create_all(engine)

# Prueba de concepto: instanciar un objeto de cada clase. Todavia no
# usamos sesiones (eso se vera en la proxima unidad), asi que esto NO
# se guarda en la base, solo confirma que las clases y sus tipos de
# columna estan bien definidos.
dataset_ejemplo = Dataset(
    name="ventas_2024",
    source_url="https://ejemplo.com/ventas_2024.csv",
    num_rows=15000,
)

modelo_ejemplo = ModelExperiment(
    algorithm_name="RandomForestRegressor",
    accuracy=0.87,
    is_deployed=False,
)

print("Mapeo verificado:")
print(dataset_ejemplo)
print(modelo_ejemplo)
print("\nBase de datos generada en: analytics.db")
