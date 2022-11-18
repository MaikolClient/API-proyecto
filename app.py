from fastapi import FastAPI
from routes.user import user
from routes.materia import materia


app = FastAPI()

app.include_router(user)
app.include_router(materia)

