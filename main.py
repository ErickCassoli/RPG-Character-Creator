from fastapi import FastAPI
from app.routes import character_routes

app = FastAPI()

# Incluir as rotas
app.include_router(character_routes.router)
