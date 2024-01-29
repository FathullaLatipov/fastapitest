from sqlalchemy import Column, String, Integer, DateTime, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String)
    phone_number = Column(Integer, unique=True)
    level = Column(String, default='None')
    datetime = Column(DateTime)


# Таблица вопросов
class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, unique=True)
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(String, nullable=False)
    timer = Column(Date)


# Таблица результатов
class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    correct_answers = Column(Integer, default=0)
    level = Column(String)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')

# Ответы пользователя на вопросы
class UserAnswers(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id')) #2
    q_id = Column(Integer, ForeignKey('questions.id')) # 5
    level = Column(String, ForeignKey('users.level')) # 2.JUNIOR
    user_answer = Column(String)
    correctness = Column(Boolean, default=False)
    timer = Column(Date)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    question_fk = relationship(Questions, foreign_keys=[q_id], lazy='subquery')
