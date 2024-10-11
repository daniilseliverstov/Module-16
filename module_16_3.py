from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
def add_user(username: str, age: int):
    user_id = str(max(int(id) for id in users.keys()) + 1)
    user_info = f'Имя: {username}, возраст: {age}'
    users[user_id] = user_info
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    user_info = f'Имя: {username}, возраст: {age}'
    users[user_id] = user_info
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    del users[user_id]
    return f'User {user_id} is deleted'
