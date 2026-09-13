from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
vectors_router = APIRouter(prefix=Prefix.ALGEBRA.value)

@vectors_router.get(Endpoints.VECTORS.value, response_class=HTMLResponse)
def vectors(request: Request) -> HTMLResponse:

    vectors_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.VECTORS.value,
        request=request,
    )
    return vectors_template
