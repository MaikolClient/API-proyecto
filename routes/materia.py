from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from models.materia import materias
from schemas.materia import Materia

materia = APIRouter()


@materia.get("/materias", response_model=list[Materia], tags=["Materias"])
def get_materias():
    return conn.execute(materias.select()).fetchall()

@materia.post("/materias", response_model=Materia, tags=["Materias"])
def create_materia(materia: Materia):
    new_materia = {"nombre": materia.nombre}
    result = conn.execute(materias.insert().values(new_materia))
    return conn.execute(materias.select().where(materias.c.id == result.lastrowid)).first()

@materia.get("/materia/{id}", response_model=Materia, tags=["Materias"])
def get_materia(id: str):
    return conn.execute(materias.select().where(materias.c.id == id)).first()

@materia.delete("/materias/{id}",status_code=HTTP_204_NO_CONTENT, tags=["Materias"])
def delete_materia(id: str):
    result = conn.execute(materias.delete().where(materias.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@materia.put("/materias/{id}", response_model=Materia, tags=["Materias"])
def update_user(id: str, materia: Materia):
    conn.execute(materias.update().values(nombre=materia.nombre).where(materias.c.id == id))
    return conn.execute(materias.select().where(materias.c.id == id)).first()