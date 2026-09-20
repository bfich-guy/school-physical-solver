from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
mean_router = APIRouter(prefix=Prefix.ALGEBRA.value)

@mean_router.get(Endpoints.MEAN.value, response_class=HTMLResponse)
def mean(request: Request) -> HTMLResponse:

    mean_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.MEAN.value,
        request=request,
    )
    return mean_template
