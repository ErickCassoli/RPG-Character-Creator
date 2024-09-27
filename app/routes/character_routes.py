from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.character_schema import Character as CharacterSchema
from app.models.character_model import Character as CharacterModel
from app.config import get_db

router = APIRouter()

# Criar um personagem e salvar no banco de dados
@router.post("/characters", response_model=CharacterSchema)
def create_character(character: CharacterSchema, db: Session = Depends(get_db)):
    db_character = CharacterModel(
        nickname=character.nickname,
        player_name=character.player.name,
        xp=character.xp,
        race=character.race,
        classes=character.classes,
        background=character.background.model_dump(),
        details=character.details.model_dump() if character.details else None,
        weapon_proficiencies=character.weapon_proficiencies,
        armor_proficiencies=character.armor_proficiencies,
        tool_proficiencies=character.tool_proficiencies,
        feats=character.feats,
        spells=character.spells,
        weapons=character.weapons,
        equipment=character.equipment,
        treasure=character.treasure,
    )
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

# Listar todos os personagens do banco de dados
@router.get("/characters", response_model=List[CharacterSchema])
def get_characters(db: Session = Depends(get_db)):
    return db.query(CharacterModel).all()
