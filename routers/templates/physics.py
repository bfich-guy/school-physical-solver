from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
physics_router = APIRouter(prefix=Prefix.INDEX.value)

@physics_router.get(Endpoints.PHYSICS.value, response_class=HTMLResponse)
def physics(request: Request) -> HTMLResponse:

    physics_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.PHYSICS.value,
        request=request,
    )
    return physics_template
