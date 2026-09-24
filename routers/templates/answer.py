from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
answer_router = APIRouter(prefix=Prefix.INDEX.value)

@answer_router.get(Endpoints.ANSWER.value, response_class=HTMLResponse)
def answer(request: Request) -> HTMLResponse:

    answer_template: HTMLResponse = templates.TemplateResponse(
            name=Templates.ANSWER.value,
            request=request,
        )
    return answer_template
