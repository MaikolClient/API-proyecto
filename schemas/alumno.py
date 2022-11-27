from pydantic import BaseModel
from typing import Optional

class Alumno(BaseModel):
    id: Optional[str]
    rut: str
    nombre: str
    email: str
    password: str