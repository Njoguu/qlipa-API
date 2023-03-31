from src import database
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from http.client import CREATED, OK


class PSV(BaseModel):
    psv_id: int
    registration_no: str
    driver: str
    seats: int
    route_id: int
    owner_id: int
    fare: int
    date_created: str


app = FastAPI()


# PSVs --> Only psv owners should be able to perform operations on these endpoints
# get List of psvs
@app.get("/psvs", tags=['PSVs'])
def get_all_psvs():

    return {
        "message": "Data Retrieved Sussessfully!",
        "data": database.getData()
    }, OK


@app.post("/psv", tags=['PSVs'], response_model=PSV)
async def add_new_psv(psv: PSV):

    try:
        database.addData()
        return {
            "message": "Added Successfully!",
            "PSV": {
                "psv_id": PSV.psv_id,
                "reg_no": PSV.registration_no,
            }
        }, CREATED
    except Exception as err:
        return {
            "message": f"Could not add data! {err}"
        }


@app.put("/psv/{psv_id}", tags=['PSVs'])
async def update_existing_psv(psv_id: int):
    return {
        ...
    }, OK


@app.delete("/psv/{psv_id}", tags=['PSVs'])
async def delete_existing_psv(psv_id: int):
    return {
        ...
    }, OK
