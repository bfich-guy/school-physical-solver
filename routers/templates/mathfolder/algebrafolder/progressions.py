from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
progressions_router = APIRouter(prefix=Prefix.ALGEBRA.value)

@progressions_router.get(Endpoints.PROGRESSIONS.value, response_class=HTMLResponse)
def progressions(request: Request) -> HTMLResponse:

    progressions_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.PROGRESSIONS.value,
        request=request,
    )
    return progressions_template
