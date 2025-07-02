from fastapi import APIRouter
from sqlmodel import Session, select
from ..models.models import User
from ..db import get_session
from fastapi import Depends

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/postuser", response_model=User)
def create_user(user: User,session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id);
    return user











    