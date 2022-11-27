from pydantic import BaseModel
from typing import Optional

class Profesor(BaseModel):
    id: Optional[str]
    rut: str
    nombre: str
    email: str
    password: str