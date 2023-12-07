from datetime import date
from sqlalchemy import and_, delete, func, insert, or_, select

from app.bookings.models import Bookings

from app.services.base import BaseDAO
from app.database import async_session_maker, engine


class BookingDAO(BaseDAO):
    model = Bookings
