from sqlalchemy import Column, Integer, String, JSON
from app.config import Base

class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, index=True)
    player_name = Column(String)
    xp = Column(Integer, default=0)
    race = Column(String)
    classes = Column(JSON)
    background = Column(JSON)
    details = Column(JSON)
    weapon_proficiencies = Column(JSON)
    armor_proficiencies = Column(JSON)
    tool_proficiencies = Column(JSON)
    feats = Column(JSON)
    spells = Column(JSON)
    weapons = Column(JSON)
    equipment = Column(JSON)
    treasure = Column(JSON)
