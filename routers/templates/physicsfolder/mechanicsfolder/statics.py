from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
statics_router = APIRouter(prefix=Prefix.MECHANICS.value)

@statics_router.get(Endpoints.STATICS.value, response_class=HTMLResponse)
def statics(request: Request) -> HTMLResponse:

    statics_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.STATICS.value,
        request=request,
    )
    return statics_template
