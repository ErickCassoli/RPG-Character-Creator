from app.config import engine, Base
from app.models.character_model import Character

Base.metadata.create_all(bind=engine)
