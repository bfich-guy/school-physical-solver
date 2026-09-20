from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
magnetism_router = APIRouter(prefix=Prefix.ELECTROMAGNETICS.value)

@magnetism_router.get(Endpoints.MAGNETISM.value, response_class=HTMLResponse)
def magnetism(request: Request) -> HTMLResponse:

    magnetism_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.MAGNETISM.value,
        request=request,
    )
    return magnetism_template
