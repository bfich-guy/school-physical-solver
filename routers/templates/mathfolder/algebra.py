from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
algebra_router = APIRouter(prefix=Prefix.MATH.value)

@algebra_router.get(Endpoints.ALGEBRA.value, response_class=HTMLResponse)
def algebra(request: Request) -> HTMLResponse:

    algebra_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.ALGEBRA.value,
        request=request,
    )
    return algebra_template
