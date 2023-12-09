from pydantic import BaseModel, Json


class SHotels(BaseModel):
    id: int 
    name: str 
    location: str 
    services: list[str]
    rooms_quantity: int 
    image_id: int


class SHotelsInfo(SHotels):
    rooms_left: int
