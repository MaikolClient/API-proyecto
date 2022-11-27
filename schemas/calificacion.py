from pydantic import BaseModel
from typing import Optional

class Calificacion(BaseModel):
    id: Optional[str]
    id_profesor: str
    id_alumno: str
    id_materia: str
    valoracion: str 
