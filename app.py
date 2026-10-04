from uvicorn import run
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from system.config.constants import Folders, Mounts
from system.utils.systemserverhelpers import include_routers

from routers.templates.index import index_router
from routers.calculate import calculate_router

from routers.templates.aboutus.extrainfo import extrainfo_router
from routers.templates.aboutus.faq import faq_router 
from routers.templates.aboutus.usagepolicy import usage_policy_router

from routers.templates.math.algebra import algebra_router
from routers.templates.math.geometry import geometry_router

from routers.templates.physics.electromagnetics import electromagnetics_router
from routers.templates.physics.mechanics import mechanics_router
from routers.templates.physics.thermodynamics import thermodynamics_router


app = FastAPI()

"""
origins_list: list[str] = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "https://school-physmath-solver.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
"""

routers_list: list[APIRouter] = [
    index_router,
    calculate_router,

    extrainfo_router,
    faq_router,
    usage_policy_router,

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

server_is_launching_directly: bool = __name__ == "__main__"

if server_is_launching_directly:
    run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
