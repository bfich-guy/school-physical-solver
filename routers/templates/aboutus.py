from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
aboutus_router = APIRouter(prefix=Prefix.INDEX.value)

@aboutus_router.get(Endpoints.ABOUTUS.value, response_class=HTMLResponse)
def aboutus(request: Request) -> HTMLResponse:

    aboutus_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.ABOUTUS.value,
        request=request,
    )
    return aboutus_template
