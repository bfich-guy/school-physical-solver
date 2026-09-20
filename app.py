from uvicorn import run
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from system.config.system import Folders
from system.config.server import Mounts

from system.utils.server import include_routers

from routers.templates.index import index_router

from routers.templates.aboutusrouter.extrainfo import extrainfo_router
from routers.templates.aboutusrouter.faq import faq_router 
from routers.templates.aboutusrouter.usagepolicy import usage_policy_router

from routers.templates.math import math_router
from routers.templates.physics import physics_router

from routers.templates.mathfolder.algebra import algebra_router
from routers.templates.mathfolder.geometry import geometry_router

from routers.templates.physicsfolder.electromagnetics import electromagnetics_router
from routers.templates.physicsfolder.mechanics import mechanics_router
from routers.templates.physicsfolder.thermodynamics import thermodynamics_router

from routers.templates.mathfolder.algebrafolder.equations import equations_router
from routers.templates.mathfolder.algebrafolder.functions import functions_router
from routers.templates.mathfolder.algebrafolder.mean import mean_router
from routers.templates.mathfolder.algebrafolder.progressions import progressions_router
from routers.templates.mathfolder.algebrafolder.vectors import vectors_router

from routers.templates.mathfolder.geometryfolder.circles import circles_router
from routers.templates.mathfolder.geometryfolder.parallelograms import parallelograms_router
from routers.templates.mathfolder.geometryfolder.polygons import polygons_router
from routers.templates.mathfolder.geometryfolder.trapezoids import trapezoids_router
from routers.templates.mathfolder.geometryfolder.triangles import triangles_router

from routers.templates.physicsfolder.electromagneticsfolder.electricity import electricity_router
from routers.templates.physicsfolder.electromagneticsfolder.magnetism import magnetism_router

from routers.templates.physicsfolder.mechanicsfolder.dynamics import dynamics_router
from routers.templates.physicsfolder.mechanicsfolder.kinematics import kinematics_router
from routers.templates.physicsfolder.mechanicsfolder.statics import statics_router


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

    extrainfo_router,
    faq_router,
    usage_policy_router,

    math_router,
    physics_router,

    algebra_router,
    geometry_router,
    electromagnetics_router,
    mechanics_router,
    thermodynamics_router,

    equations_router,
    functions_router,
    mean_router,
    progressions_router,
    vectors_router,

    circles_router,
    parallelograms_router,
    polygons_router,
    trapezoids_router,
    triangles_router,

    electricity_router,
    magnetism_router,

    dynamics_router,
    kinematics_router,
    statics_router,
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
