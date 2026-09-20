from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
electricity_router = APIRouter(prefix=Prefix.ELECTROMAGNETICS.value)

@electricity_router.get(Endpoints.ELECTRICITY.value, response_class=HTMLResponse)
def electricity(request: Request) -> HTMLResponse:

    electricity_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.ELECTRICITY.value,
        request=request,
    )
    return electricity_template
