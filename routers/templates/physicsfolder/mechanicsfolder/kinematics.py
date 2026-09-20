from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints, Templates


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
kinematics_router = APIRouter(prefix=Prefix.MECHANICS.value)

@kinematics_router.get(Endpoints.KINEMATICS.value, response_class=HTMLResponse)
def kinematics(request: Request) -> HTMLResponse:

    kinematics_template: HTMLResponse = templates.TemplateResponse(
        name=Templates.KINEMATICS.value,
        request=request,
    )
    return kinematics_template
