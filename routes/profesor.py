from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from models.profesor import profesores
from schemas.profesor import Profesor
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
profesor = APIRouter()


@profesor.get("/profesores", response_model=list[Profesor], tags=["Profesores"])
def get_profesores():
    return conn.execute(profesores.select()).fetchall()

@profesor.post("/profesores", response_model=Profesor, tags=["Profesores"])
def create_profesor(profesor: Profesor):
    new_profesor = {"rut": profesor.rut, 
                    "nombre": profesor.nombre, 
                    "email": profesor.email}
    new_profesor["password"] = f.encrypt(profesor.password.encode("utf-8"))
    result = conn.execute(profesores.insert().values(new_profesor))
    return conn.execute(profesores.select().where(profesores.c.id == result.lastrowid)).first()


@profesor.get("/profesores/{id}", response_model=Profesor, tags=["Profesores"])
def get_profesor(id: str):
    return conn.execute(profesores.select().where(profesores.c.id == id)).first()


@profesor.delete("/profesores/{id}",status_code=HTTP_204_NO_CONTENT, tags=["Profesores"])
def delete_profesor(id: str):
    result = conn.execute(profesores.delete().where(profesores.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@profesor.put("/profesores/{id}", response_model=Profesor, tags=["Profesores"])
def update_profesor(id: str, profesor: Profesor):
    conn.execute(profesores.update().values(nombre=profesor.nombre, email=profesor.email,
                 password=f.encrypt(profesor.password.encode("utf-8"))).where(profesores.c.id == id))
    return conn.execute(profesores.select().where(profesores.c.id == id)).first()
