from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String, VARCHAR

calificaciones = Table("calificaciones", meta, Column(
    "id", Integer, primary_key=True),
    Column("id_profesor", VARCHAR(9)),
    Column("id_alumno", VARCHAR(9)),
    Column("id_materia", VARCHAR(9)),
    Column("valoracion", VARCHAR(9)))

meta.create_all(engine)