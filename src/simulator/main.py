from typing import Any

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from simulator.config import Config
from simulator.global_setting import GlobalSetting

app = FastAPI()


# Define a Pydantic model to validate the incoming JSON body
class DataModel(BaseModel):
    configuration: dict[Any, Any]


# Define a POST route to handle incoming JSON data
@app.post("/process")
async def process_data(data: DataModel):
    parameters_dict = data.configuration

    config = Config(parameters_dict)
    setting = GlobalSetting(config)

    return JSONResponse(content=setting.global_log)
