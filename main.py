from fastapi import FastAPI

# Для запуска проекта надо писать такую комнаду как
# uvicorn FILENAME:app --reload

app = FastAPI(docs_url='/')
