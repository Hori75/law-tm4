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

@app.post("/update")
async def update(param: schemas.MahasiswaBase = None, db: Session = Depends(get_db)):
    res = db.query(models.Mahasiswa).filter(models.Mahasiswa.npm == param.npm).first()
    if (res != None):
        res.nama = param.nama
        db.add(res)
        db.commit()
    else:
        db_mahasiswa = models.Mahasiswa(
            npm = param.npm,
            nama = param.nama
        )
        db.add(db_mahasiswa)
        db.commit()
    
    return {
        "status": 'OK',
        'npm': param.npm,
        'nama': param.nama
    }
