from typing import Union

from pydantic import BaseModel


class PatternBase(BaseModel):
    pattern_name: str
    description: Union[str, None] = None


class PatternCreate(PatternBase):
    pass


class Pattern(PatternBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Pattern] = []

    class Config:
        orm_mode = True
