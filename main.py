from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title= "API de Tarefas")

class taferas(BaseModel):
    id: Optional [int] = None
    titulo: str
    descrição: str
    concluida: bool = False

db_tarefas = []
