from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
extrainfo_router = APIRouter(prefix=Prefix.INDEX.value)

@extrainfo_router.get(Endpoints.EXTRAINFO.value, response_class=HTMLResponse)
def extrainfo(request: Request) -> HTMLResponse:

    extrainfo_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.EXTRAINFO.value,
        request=request,
    )
    return extrainfo_template
