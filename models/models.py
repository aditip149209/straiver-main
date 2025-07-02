from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
class User(SQLModel, table= True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    email: str
    questions: List["Question"] = Relationship(back_populates="user")
    answers: List["Answer"] = Relationship(back_populates="user")


class Question():
    question_id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    user_id: int = Field(foreign_key="user.user_id")
    user: Optional["User"] = Relationship(back_populates="questions")
    answer: List["Answer"] = Relationship(back_populates="question");


class Answer():
    answer_id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    user_id: int = Field(foreign_key="user.user_id")
    question_id: int = Field(foreign_key="question.question_id")
    user: Optional["User"] = Relationship(back_populates="answers")
    question: Optional["Question"] = Relationship(back_populates="answer")





