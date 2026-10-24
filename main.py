from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title= "API de Tarefas")

class Tarefas(BaseModel):
    id: Optional [int] = None
    titulo: str
    descrição: str
    concluida: bool = False

db_tarefas = []

@app.get("/tarefas",response_model=List[Tarefas])

async def listar_taferas():
    return db_tarefas

@app.post("/tarefas",response_model=Tarefas, status_code= 201)
async def criar_tarefa(tarefa: Tarefas):
    tarefa.id = len(db_tarefas) +1
    db_tarefas.append(tarefa)
    return tarefa
