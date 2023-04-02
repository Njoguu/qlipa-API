from typing import List
from src import database
from fastapi import FastAPI
from pydantic import BaseModel
from http.client import CREATED, OK, INTERNAL_SERVER_ERROR


class PSV(BaseModel):
    registration_no: str
    driver: str
    seats: int
    route_id: int
    owner_id: int
    fare: int


app = FastAPI()


# PSVs --> Only psv owners should be able to perform operations on these endpoints
# get List of psvs
@app.get("/psvs", tags=['PSVs'])
def get_all_psvs():

    return {
        "message": "Data Retrieved Sussessfully!",
        "data": database.getData()
    }, OK


@app.get("/psv/{psv_id}", tags=['PSVs'])
async def get_specific_PSV(psv_id: int):

    try:
        data = database.getPSV(psv_id)
        return {
            "status": "success",
            "message": "Data Retrieved Sussessfully",
            "data": data
        }, OK

    except Exception as err:
        return {
            "status": "error",
            "message": f"Could not retrieve data! {err}"
        }, INTERNAL_SERVER_ERROR


@app.post("/psv", tags=['PSVs'])
async def add_new_psv(
    registration_no: str,
    driver: str,
    seats: int,
    route_id: int,
    owner_id: int,
    fare: int,
):

    try:
        database.addData(registration_no, driver, seats,
                         route_id, owner_id, fare)
        return {
            "status": "success",
            "message": "PSV created successfully!"
        }, CREATED

    except Exception as err:
        return {
            "status": "error",
            "message": f"Could not add data! {err}"
        }, INTERNAL_SERVER_ERROR


@app.patch("/psv/{psv_id}", tags=['PSVs'])
async def update_existing_psv(
    psv_id: int,
    registration_no: str,
    driver: str,
    seats: int,
    route_id: int,
    owner_id: int,
    fare: int,
    ):

    try:
        database.updatePSV(psv_id, registration_no, driver, seats, route_id, owner_id, fare)

        return {
            "status": "success",
            "message": "Data updated successfully!"
        }, OK

    except Exception as err:
        return {
            "status": "error",
            "message": f"Could not update data! {err}"
        }, INTERNAL_SERVER_ERROR


@app.delete("/psv/{psv_id}", tags=['PSVs'])
async def delete_existing_psv(psv_id: int):
    try:
        database.deletePSV(psv_id)

        return {
            "status": "success",
            "message": "Deletion successful!",
        }, OK

    except Exception as err:
        return {
            "status": "error",
            "message": "Could not delete data! {err}"
        }, INTERNAL_SERVER_ERROR
