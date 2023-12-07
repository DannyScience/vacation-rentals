from datetime import date
from sqlalchemy import and_, delete, func, insert, or_, select

from app.bookings.models import Bookings

from app.services.base import BaseDAO
from app.database import async_session_maker, engine


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()