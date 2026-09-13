from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
mechanics_router = APIRouter(prefix=Prefix.PHYSICS.value)

@mechanics_router.get(Endpoints.MECHANICS.value, response_class=HTMLResponse)
def mechanics(request: Request) -> HTMLResponse:

    mechanics_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.MECHANICS.value,
        request=request,
    )
    return mechanics_template
