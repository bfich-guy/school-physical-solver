from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
dynamics_router = APIRouter(prefix=Prefix.MECHANICS.value)

@dynamics_router.get(Endpoints.DYNAMICS.value, response_class=HTMLResponse)
def dynamics(request: Request) -> HTMLResponse:

    dynamics_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.DYNAMICS.value,
        request=request,
    )
    return dynamics_template
