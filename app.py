from fastapi import FastAPI
from routes.alumno import alumno
from routes.materia import materia
from routes.profesor import profesor
from routes.calificacion import calificacion
from routes.agenda import agenda


app = FastAPI()

app.include_router(alumno)
app.include_router(materia)
app.include_router(profesor)
app.include_router(calificacion)
app.include_router(agenda)

