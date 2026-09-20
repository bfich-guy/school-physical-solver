from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
usage_policy_router = APIRouter(prefix=Prefix.INDEX.value)

@usage_policy_router.get(Endpoints.USAGEPOLICY.value, response_class=HTMLResponse)
def usage_policy(request: Request) -> HTMLResponse:

    usage_policy_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.USAGEPOLICY.value,
        request=request,
    )
    return usage_policy_template
