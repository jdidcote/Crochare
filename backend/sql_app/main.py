from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = APIRouter(tags=["CRUD"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/patterns/{pattern_id}/patterns/", response_model=schemas.Pattern)
def create_pattern_for_user(
    user_id: int, pattern: schemas.PatternCreate, db: Session = Depends(get_db)
):
    return crud.create_user_pattern(db=db, pattern=pattern, user_id=user_id)


@app.get("/patterns/", response_model=list[schemas.Pattern])
def read_patterns(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patterns = crud.get_patterns(db, skip=skip, limit=limit)
    return patterns
