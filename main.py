from fastapi import FastAPI

# Для запуска проекта надо писать такую комнаду как
# uvicorn FILENAME:app --reload

app = FastAPI(docs_url='/')


@app.get('/home')
def main():
    return {'Message': 'Hello'}


@app.get('/diyor', tags=['Ученики'])
def diyor():
    return {'Username': 'Diyor',
            'Age': 16,
            'Laptop': 'Asus'
            }


@app.post('/send')
async def send(username: str, age: int):
    return {f'This username: {username} and his age: {age}'}


@app.get('/muhammad', tags=['Ученики'], description='Этот метод что бы получить данные у Мухаммада')
def diyor():
    return {'Username': 'Muhammad',
            'Age': 18,
            'Laptop': 'Asus'
            }


@app.put('/changes')
async def changes(username: str, age: int):
    return {f'Username: {username} age: {age}'}


@app.patch('/change')
def change():
    return {'Username': 'Change'}


@app.delete('/remove', tags=['sdfsdf'])
async def remove(username: str, age: int):
    return {f'Удалено из базы этот {username} пользователь и ему было {age} лет'}

# Параметры для запроса
@app.get('/example')
async def example_test(user_id: int, user_answer: str, price: int):
    return {'message': f'У нашего пользователя с этим {user_id} айди примерно набрал 10 баллов и его ответ {user_answer} и он'
                       f'заплатил {price} $'}