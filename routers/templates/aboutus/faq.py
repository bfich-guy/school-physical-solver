from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.constants import Folders, Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
faq_router = APIRouter(prefix=Prefix.INDEX.value)

@faq_router.get(Endpoints.FAQ.value, response_class=HTMLResponse)
def faq(request: Request) -> HTMLResponse:

    faq_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.FAQ.value,
        request=request,
    )
    return faq_template
