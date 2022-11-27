from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from models.calificacion import calificaciones
from schemas.calificacion import Calificacion

calificacion = APIRouter()


@calificacion.get("/calificaciones", response_model=list[Calificacion], tags=["Calificaciones"])
def get_calificaciones():
    return conn.execute(calificaciones.select()).fetchall()

@calificacion.post("/calificaciones", response_model=Calificacion, tags=["Calificaciones"])
def create_calificacion(calificacion: Calificacion):
    new_calificacion = {
                        "id_profesor": calificacion.id_profesor,
                        "id_alumno": calificacion.id_alumno,
                        "id_materia": calificacion.id_materia, 
                        "valoracion": calificacion.valoracion,}
    result = conn.execute(calificaciones.insert().values(new_calificacion))
    return conn.execute(calificaciones.select().where(calificaciones.c.id == result.lastrowid)).first()

@calificacion.get("/calificaciones/{id}", response_model=Calificacion, tags=["Calificaciones"])
def get_calificacion(id: str):
    return conn.execute(calificaciones.select().where(calificaciones.c.id == id)).first()

@calificacion.delete("/calificaciones/{id}",status_code=HTTP_204_NO_CONTENT, tags=["Calificaciones"])
def delete_calificacion(id: str):
    result = conn.execute(calificaciones.delete().where(calificaciones.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@calificacion.put("/calificaciones/{id}", response_model=Calificacion, tags=["Calificaciones"])
def update_calificacion(id: str, calificacion: Calificacion):
    conn.execute(calificaciones.update().values(valoracion=calificacion.valoracion).where(calificaciones.c.id == id))
    return conn.execute(calificaciones.select().where(calificaciones.c.id == id)).first()