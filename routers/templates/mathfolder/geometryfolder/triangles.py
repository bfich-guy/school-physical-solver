from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
triangles_router = APIRouter(prefix=Prefix.GEOMETRY.value)

@triangles_router.get(Endpoints.TRIANGLES.value, response_class=HTMLResponse)
def triangles(request: Request) -> HTMLResponse:

    triangles_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.TRIANGLES.value,
        request=request,
    )
    return triangles_template
