from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
geometry_router = APIRouter(prefix=Prefix.MATH.value)

@geometry_router.get(Endpoints.GEOMETRY.value, response_class=HTMLResponse)
def algebra(request: Request) -> HTMLResponse:

    geometry_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.GEOMETRY.value,
        request=request,
    )
    return geometry_template
