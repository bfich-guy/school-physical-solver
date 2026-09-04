from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.system import Folders
from config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
math_router = APIRouter(prefix=Prefix.INDEX.value)

@math_router.get(Endpoints.MATH.value, response_class=HTMLResponse)
def math(request: Request) -> HTMLResponse:

    math_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.MATH.value,
        request=request,
    )
    return math_template
