from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from models.agenda import agendas
from schemas.agenda import Agenda 

agenda = APIRouter()


@agenda.get("/agenda", response_model=list[Agenda], tags=["Agenda"])
def get_agenda():
    return conn.execute(agendas.select()).fetchall()

@agenda.post("/agenda", response_model=Agenda, tags=["Agenda"])
def create_agenda(agenda: Agenda):
    new_agenda = {
                        "id_profesor": agenda.id_profesor,
                        "id_materia": agenda.id_materia,
                        "fecha": agenda.fecha}
    result = conn.execute(agendas.insert().values(new_agenda))
    return conn.execute(agendas.select().where(agendas.c.id == result.lastrowid)).first()

@agenda.get("/agenda/{id}", response_model=Agenda, tags=["Agenda"])
def get_agenda(id: str):
    return conn.execute(agendas.select().where(agendas.c.id == id)).first()

@agenda.delete("/agenda/{id}",status_code=HTTP_204_NO_CONTENT, tags=["Agenda"])
def delete_agenda(id: str):
    result = conn.execute(agendas.delete().where(agendas.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@agenda.put("/agenda/{id}", response_model=Agenda, tags=["Agenda"])
def update_agenda(id: str, agenda: Agenda):
    conn.execute(agendas.update().values(fecha=agenda.fecha).where(agendas.c.id == id))
    return conn.execute(agendas.select().where(agendas.c.id == id)).first()