from app.bookings.models import Bookings
from app.services.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings

        