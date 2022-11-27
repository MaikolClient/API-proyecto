from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from models.alumno import alumnos
from schemas.alumno import Alumno
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
alumno = APIRouter()


@alumno.get("/alumnos", response_model=list[Alumno], tags=["Alumnos"])
def get_alumnos():
    return conn.execute(alumnos.select()).fetchall()

@alumno.post("/alumnos", response_model=Alumno, tags=["Alumnos"])
def create_alumno(alumno: Alumno):
    new_alumno = {"rut": alumno.rut, "nombre": alumno.nombre, "email": alumno.email}
    new_alumno["password"] = f.encrypt(alumno.password.encode("utf-8"))
    result = conn.execute(alumnos.insert().values(new_alumno))
    return conn.execute(alumnos.select().where(alumnos.c.id == result.lastrowid)).first()


@alumno.get("/alumnos/{id}", response_model=Alumno, tags=["Alumnos"])
def get_alumno(id: str):
    return conn.execute(alumnos.select().where(alumnos.c.id == id)).first()


@alumno.delete("/alumnos/{id}",status_code=HTTP_204_NO_CONTENT, tags=["Alumnos"])
def delete_alumno(id: str):
    result = conn.execute(alumnos.delete().where(alumnos.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@alumno.put("/alumnos/{id}", response_model=Alumno, tags=["Alumnos"])
def update_alumno(id: str, alumno: Alumno):
    conn.execute(alumnos.update().values(name=alumno.name, email=alumno.email,
                 password=f.encrypt(alumno.password.encode("utf-8"))).where(alumnos.c.id == id))
    return conn.execute(alumnos.select().where(alumnos.c.id == id)).first()
