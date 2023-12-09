from datetime import date, timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Query

from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotels, SHotelsInfo
from app.exceptions import BackToTheFuture, BookingNotFound, TooLongBooking


router = APIRouter(
    prefix='/hotels',
    tags=['Hotels and rooms']
)


@router.get('')
async def get_hotels_by_location_and_time(
    location: Annotated[
        str,
        Query(
            description="Ex, Altai",
        ),
    ],
    date_from: Annotated[
        date, Query(description=f"Ex, {datetime.now().date()}")
    ] = ...,
    date_to: Annotated[
        date, Query(description=f"Ex, {datetime.now().date()}")
    ] = ...,
) -> list[SHotelsInfo]:
    if date_from > date_to:
        raise BackToTheFuture
    if date_to - date_from > timedelta(days=30):
        raise TooLongBooking

    return await HotelDAO.find_all(location, date_from, date_to)


@router.get('/id/{hotel_id}')
async def get_hotel_by_id(hotel_id: int) -> SHotels:
    result =  await HotelDAO.find_by_id(hotel_id)
    if not result:
        raise BookingNotFound
    return result
