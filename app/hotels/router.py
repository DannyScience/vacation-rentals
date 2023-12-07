from fastapi import APIRouter


router = APIRouter(
    prefix='/hotels',
    tags=['Hotels and rooms']
)


@router.get('')
def get_hotels():
    pass
