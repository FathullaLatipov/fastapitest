from fastapi import FastAPI

# Для запуска проекта надо писать такую комнаду как
# uvicorn FILENAME:app --reload
from api.test_api.tests import test_router
from api.user_api.users import user_router

from database import Base, engine
Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(test_router)


