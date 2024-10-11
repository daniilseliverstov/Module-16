from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users = []


@app.get('/users')
def get_users():
    return users


@app.post('/user/{username}/{age}')
def add_user(username: str, age: int):
    if not users:
        user_id = 1
    else:
        user_id = max(user.id for user in users) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")