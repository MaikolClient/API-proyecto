from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String

materias = Table("materias", meta, Column(
    "id", Integer, primary_key=True),
    Column("nombre", String(255)))

meta.create_all(engine)
