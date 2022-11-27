from fastapi import FastAPI
from routes.alumno import alumno
from routes.materia import materia
from routes.profesor import profesor
from routes.calificacion import calificacion


app = FastAPI()

app.include_router(alumno)
app.include_router(materia)
app.include_router(profesor)
app.include_router(calificacion)

