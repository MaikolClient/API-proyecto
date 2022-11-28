from pydantic import BaseModel
from typing import Optional


class Agenda(BaseModel):
    id: Optional[str]
    id_profesor: str
    id_materia: str
    fecha: str