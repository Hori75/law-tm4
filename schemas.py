from typing import Optional
from pydantic import BaseModel

class MahasiswaBase(BaseModel):
    npm: str
    nama: str

