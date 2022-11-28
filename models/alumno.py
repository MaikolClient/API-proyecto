from sqlalchemy import Table, Column
from config.db import meta,engine
from sqlalchemy.sql.sqltypes import Integer, String, VARCHAR

alumnos = Table("alumnos", meta, Column(
    "id", Integer, primary_key=True), 
    Column("rut", String(9)),
    Column("nombre", String(255)), 
    Column("email", String(255)), 
    Column("password", String(255)))

meta.create_all(engine)