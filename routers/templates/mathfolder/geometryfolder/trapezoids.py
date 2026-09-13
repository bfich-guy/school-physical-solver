from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
trapezoids_router = APIRouter(prefix=Prefix.GEOMETRY.value)

@trapezoids_router.get(Endpoints.TRAPEZOIDS.value, response_class=HTMLResponse)
def trapezoids(request: Request) -> HTMLResponse:

    trapezoids_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.TRAPEZOIDS.value,
        request=request,
    )
    return trapezoids_template
