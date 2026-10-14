from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from system.config.constants import Folders, Mounts, origins
from system.utils.systemserverhelpers import include_routers

from routers.templates.index import index_router
from routers.templates.aboutus import aboutus_router
from routers.calculate import calculate_router

from routers.templates.math.algebra import algebra_router
from routers.templates.math.geometry import geometry_router

from routers.templates.physics.electromagnetics import electromagnetics_router
from routers.templates.physics.mechanics import mechanics_router
from routers.templates.physics.thermodynamics import thermodynamics_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

routers_list: list[APIRouter] = [
    index_router,
    calculate_router,
    aboutus_router,

    algebra_router,
    geometry_router,
    electromagnetics_router,
    mechanics_router,
    thermodynamics_router,
]

include_routers(
    app=app, 
    routers_list=routers_list,
    )

app.mount(
    Mounts.STATIC.value, 
    StaticFiles(directory=Folders.STATIC.value), 
    name=Folders.STATIC.value,
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exception: RequestValidationError) -> JSONResponse:
    json_responce = JSONResponse({"answer": None})
    return json_responce
