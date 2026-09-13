from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
circles_router = APIRouter(prefix=Prefix.GEOMETRY.value)

@circles_router.get(Endpoints.CIRCLES.value, response_class=HTMLResponse)
def circles(request: Request) -> HTMLResponse:

    circles_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.CIRCLES.value,
        request=request,
    )
    return circles_template
