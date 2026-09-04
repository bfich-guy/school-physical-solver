from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.system import Folders
from config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
probstats_router = APIRouter(prefix=Prefix.MATH.value)

@probstats_router.get(Endpoints.PROBSTATS.value, response_class=HTMLResponse)
def probstats(request: Request) -> HTMLResponse:

    probstats_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.PROBSTATS.value,
        request=request,
    )
    return probstats_template
