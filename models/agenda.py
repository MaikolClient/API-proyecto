from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, Date, String

agendas = Table("agendas", meta, Column(
    "id", Integer, primary_key=True),
    Column("id_profesor", String(9)),
    Column("id_materia", String(9)),
    Column("fecha", String(255)))

meta.create_all(engine)