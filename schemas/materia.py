from pydantic import BaseModel
from typing import Optional

class Materia(BaseModel):
    id: Optional[str]
    nombre: str