from typing import Union

from pydantic import BaseModel


class PatternBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(PatternBase):
    pass


class Item(PatternBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active = True
    items: list[Item] = []

    class Config:
        orm_mode = True

