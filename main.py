from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI(
    title="Trading App"
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Vasya"},
    {"id": 2, "role": "user", "name": "Anton"},
    {"id": 2, "role": "user", "name": "Kirill"},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 321, "amount": 1.23},
]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return list(filter(lambda user: user.get("id") == user_id, fake_users))

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str, response: Response):
    filtered = list(filter(lambda user: user.get("id") == user_id, fake_users))
    if len(filtered) > 0:
        current_user = filtered[0]
        current_user["name"] = new_name
        return current_user
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "There is no user with such id"}    

class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    side: str
    price: float
    amount: float

@app.post("/trades/")
def add_trades(trades: list[Trade]):
    fake_trades.extend(trades)
    return fake_trades
    