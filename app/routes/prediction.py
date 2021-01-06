"""
Functions to predict the optimal price for an AirBnB listing.
"""
from fastapi import APIRouter
from app.schemas.listing import Listing
from app.services.price import predict_price


router = APIRouter()


@router.post('/predict')
async def predict(listing: Listing):
    """
    Make a prediction for the AirBnB Optimal Listing Price 🔮

    ### Request Body
    - `neighborhood`: neighborhood the listing is located
    - `property_type`: The type of property of the listing
    - `room_type`: The type of room of the listing
    - `accomodates`: Number of people the listing accomodates

    ### Response
    - `prediction`: float, at random

    """
    prediction = predict_price(listing)

    return prediction
