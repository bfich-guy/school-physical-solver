from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
parallelograms_router = APIRouter(prefix=Prefix.GEOMETRY.value)

@parallelograms_router.get(Endpoints.PARALLELOGRAMS.value, response_class=HTMLResponse)
def parallelograms(request: Request) -> HTMLResponse:

    parallelograms_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.PARALLELOGRAMS.value,
        request=request,
    )
    return parallelograms_template
