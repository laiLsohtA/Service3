from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Tarefa
from auth import get_current_user

router = APIRouter()

@router.get("/stats")
def get_stats(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    tarefas = db.query(Tarefa).filter(Tarefa.usuarioId == user_id).all()

    total = len(tarefas)
    concluidas = len([t for t in tarefas if t.concluida])
    pendentes = total - concluidas

    return {
        "usuarioId": user_id,
        "total": total,
        "concluidas": concluidas,
        "pendentes": pendentes
    }