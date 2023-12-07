from datetime import date
from typing import List
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import RoomCannotBeBooked
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
    ) 


class BookingsList(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int
    
    

@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):# -> List[BookingsList]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post('')
async def add_booking(
    room_id: int, date_from: date, date_to: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked


@router.delete('/{booking_id}')
async def delete_booking(
    booking_id: int,
    user: Users = Depends(get_current_user)
):
    await BookingDAO.delete_booking(booking_id, user.id)
