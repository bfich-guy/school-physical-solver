from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from system.config.system import Folders
from system.config.server import Prefix, Endpoints


templates = Jinja2Templates(directory=Folders.TEMPLATES.value)
answer_router = APIRouter(prefix=Prefix.INDEX.value)

@answer_router.get(Endpoints.ANSWER.value, response_class=JSONResponse)
def answer(request: Request) -> JSONResponse:

    
