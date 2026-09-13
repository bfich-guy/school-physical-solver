from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
functions_router = APIRouter(prefix=Prefix.ALGEBRA.value)

@functions_router.get(Endpoints.FUNCTIONS.value, response_class=HTMLResponse)
def functions(request: Request) -> HTMLResponse:

    functions_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.FUNCTIONS.value,
        request=request,
    )
    return functions_template
