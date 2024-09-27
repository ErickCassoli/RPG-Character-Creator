from pydantic import BaseModel
from typing import List, Optional

class Player(BaseModel):
    name: str
    id: Optional[str] = None

class Background(BaseModel):
    name: str
    option: Optional[str] = None
    description: Optional[str] = None
    source: Optional[str] = None

class Details(BaseModel):
    age: Optional[int] = None
    eyes: Optional[str] = None
    hair: Optional[str] = None
    skin: Optional[str] = None
    weight: Optional[int] = None
    height: Optional[str] = None
    personality: Optional[str] = None
    ideal: Optional[str] = None
    bond: Optional[str] = None
    flaw: Optional[str] = None
    backstory: Optional[str] = None
    physical: Optional[str] = None

class Character(BaseModel):
    nickname: Optional[str] = None
    player: Player
    xp: Optional[int] = 0
    race: str
    classes: List[str]
    background: Optional[Background] = None
    details: Optional[Details] = None
    weapon_proficiencies: Optional[List[str]] = None
    armor_proficiencies: Optional[List[str]] = None
    tool_proficiencies: Optional[List[str]] = None
    feats: Optional[List[str]] = None
    spells: Optional[List[str]] = None
    weapons: Optional[List[str]] = None
    equipment: Optional[List[str]] = None
    treasure: Optional[dict] = None
