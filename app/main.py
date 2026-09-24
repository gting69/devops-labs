from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import database, models

app = FastAPI(title="Реєстр бойових котів — DevOps Lab")

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"повідомлення": "Слава Україні! Реєстр бойових котів працює успішно 🐾"}

@app.get("/cats/")
def get_cats(db: Session = Depends(get_db)):
    return db.query(models.Cat).all()

@app.post("/cats/")
def create_cat(name: str, specialty: str, db: Session = Depends(get_db)):
    new_cat = models.Cat(name=name, specialty=specialty)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return {"повідомлення": "Кіт успішно зарахований до лав!", "кіт": new_cat}