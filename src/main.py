from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from http.client import CREATED, OK


class User(BaseModel):
    uid: int
    name: str
    email: str
    username: str


class PSVOWner(User):
    PSV_owned_id: int


class PSV(BaseModel):
    uid: int
    reg_no: int
    PSVOWner: int
    capacity: int
    fare_set: float


app = FastAPI()


# PSV Owners
@app.get("/owner/me", tags=['PSV Owner'])
async def get_logged_in_owner(details: PSVOWner):
    return details, OK


@app.post("/owner", tags=['PSV Owner'])
async def create_new_owner(data: PSVOWner):
    return {
        "messsage": "Account Created Successfully!",
        "data": data
    }, CREATED


@app.patch("/owner/{uid}", tags=['PSV Owner'])
async def update_owner_details(data: PSVOWner):
    return {
        "message": "Details Updated Successfully!",
        "Data": data
    }, OK


@app.delete("/owner/{uid}", tags=['PSV Owner'])
async def delete_user_account(uid):
    return {
        "message": "Account deleted Successfully",
        "Data": uid
    }, OK


# PSVs
@app.get("/psvs", tags=['PSVs'], response_model=List[PSV])
async def get_all_psvs():
    return {
        "PSVs": []
    }, OK


@app.get("/psv/{uid}", tags=['PSVs'])
async def get_PSV_data(uid):
    return {
        "PSV data": {
            "uid": uid
        }
    }, OK


# Transactions --> TODO: Add Protection to these endpoints
@app.get("/transactions/{uid}", tags=['Transactions'])
async def get_user_transactions(uid):
    return {
        "Transactions": {
            "uid": uid,
            "data": []
        }
    }, OK
