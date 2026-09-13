from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
thermodynamics_router = APIRouter(prefix=Prefix.PHYSICS.value)

@thermodynamics_router.get(Endpoints.THERMODYNAMICS.value, response_class=HTMLResponse)
def thermodynamics(request: Request) -> HTMLResponse:

    thermodynamics_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.THERMODYNAMICS.value,
        request=request,
    )
    return thermodynamics_template
