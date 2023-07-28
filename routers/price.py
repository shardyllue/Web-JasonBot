from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from fastapi import Request
from fastapi.responses import HTMLResponse


app = APIRouter(
    prefix="/info"
)

template = Jinja2Templates(
    directory="template"
)


@app.get("/")
async def price(request : Request) -> HTMLResponse:


    return template.TemplateResponse(
        name = "price.html",
        context={
            "request" : request
        },
        status_code=200
    )