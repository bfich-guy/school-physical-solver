from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
equations_router = APIRouter(prefix=Prefix.ALGEBRA.value)

@equations_router.get(Endpoints.EQUATIONS.value, response_class=HTMLResponse)
def equations(request: Request) -> HTMLResponse:

    equations_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.EQUATIONS.value,
        request=request,
    )
    return equations_template
