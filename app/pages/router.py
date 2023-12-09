from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from app.hotels.router import get_hotels_by_location_and_time


router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)


templates = Jinja2Templates(directory='app/templates')


@router.get('')
async def get_hotels(
    request: Request,
    data = Depends(get_hotels_by_location_and_time)
):
    return templates.TemplateResponse(name='hotels.html', context={'request': request, 'data': data})
