from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
polygons_router = APIRouter(prefix=Prefix.GEOMETRY.value)

@polygons_router.get(Endpoints.POLYGONS.value, response_class=HTMLResponse)
def polygons(request: Request) -> HTMLResponse:

    polygons_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.POLYGONS.value,
        request=request,
    )
    return polygons_template
