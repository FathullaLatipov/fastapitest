from fastapi import APIRouter
from database.testservice import get_20_questions_db, add_question_db, get_5_leaders_db, check_user_answer_db
from database.userservice import user_answer_db

test_router = APIRouter(prefix='/test', tags=['Работа с тестами'])


# Получить все 20 вопросов
@test_router.get('/get-20-questions')
async def get_20_questions():
    questions = get_20_questions_db()
    return questions


# Для добавлении вопросов
@test_router.post('/add-questions')
async def add_questions(main_question: str, v1: str, v2: str, v3: str, v4: str, correct_answer: str):
    add_q = add_question_db(main_question, v1, v2, v3, v4, correct_answer)
    return f'Успешно {add_q}'


# Получаем 5 лидеров
@test_router.get('/5-leaders')
async def get_5_leaders():
    leaders = get_5_leaders_db()
    return leaders


# Получаем ответы пользователя
@test_router.post('/check-answers')
async def check_answers(user_id: int, q_id: int, level: str, user_answer: str):
    user_answers = user_answer_db(user_id, q_id, level, user_answer)
    return user_answers
