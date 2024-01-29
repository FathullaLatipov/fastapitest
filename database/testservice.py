from .models import Result, Questions, UserAnswers
from database import get_db


# Получить топ 5 лидеров
def get_5_leaders_db():
    db = next(get_db())

    leaders = db.query(Result.user_id).order_by(Result.correct_answers.desc())

    return leaders[:5]


# Мы сами добавляем вопросы и варианты
def add_question_db(main_question, v1, v2, v3, v4, correct_answer):
    db = next(get_db())

    new_question = Questions(main_question=main_question, v1=v1, v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)

    db.add(new_question)
    db.commit()

    return 'Вопрос успешно добавлен'


# Получить только 20 тестов
def get_20_questions_db():
    db = next(get_db())

    question = db.query(Questions).all()

    return question[:20]


# Проверка ответа пользователя
def check_user_answer_db(user_id, q_id, user_answer):
    db = next(get_db())

    current_question = db.query(UserAnswers).filter_by(user_id=user_id, q_id=q_id, user_answer=user_answer).first()

    if current_question:
        db.add(current_question)
        db.commit()
        return True
    else:
        return False
