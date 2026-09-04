from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.system import Folders
from config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
electromagnetics_router = APIRouter(prefix=Prefix.PHYSICS.value)

@electromagnetics_router.get(Endpoints.ELECTROMAGNETICS.value, response_class=HTMLResponse)
def electromagnetics(request: Request) -> HTMLResponse:

    electromagnetics_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.ELECTROMAGNETICS.value,
        request=request,
    )
    return electromagnetics_template
