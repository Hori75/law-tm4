from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/ping")
async def root():
    return "phong"

@app.get("/read/{npm}")
async def read(npm: str, db: Session = Depends(get_db)):
    return get_by_npm(npm, db)

@app.get("/read/{npm}/{txid}")
async def read(npm: str, txid: str, db: Session = Depends(get_db)):
    return get_by_npm(npm, db)

def get_by_npm(npm: str, db: Session = Depends(get_db)):
    res = db.query(models.Mahasiswa).filter(models.Mahasiswa.npm == npm).first()
    return {
        'npm': res.npm,
        'nama': res.nama
    }
