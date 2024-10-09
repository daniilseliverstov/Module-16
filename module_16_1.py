import fastapi

app = fastapi.FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {'message': 'Главная страница'}
