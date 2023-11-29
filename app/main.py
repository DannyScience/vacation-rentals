from fastapi import FastAPI

app = FastAPI()


@app.get('/rentals')
def get_rentals():
    return 'Rentals in your area:'
