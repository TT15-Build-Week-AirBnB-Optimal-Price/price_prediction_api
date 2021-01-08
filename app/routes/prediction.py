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
    - `host_id`: ID number for the host who posted the listing
    - `last_review`: Julian date of the last review posted for the listing
    - `minimum_nights`: Mininum number of nights that can be booked
    - `latitude`: The latitude of the property
    - `minimum_nights_avg_ntm`: Not sure... but it seemed important
    - `first_review`: Julian date of the first review posted for the listing
    - `bedrooms`: Number of bedrooms
    - `number_of_reviews`: Number of reviews the listing has received 
    - `num_baths`: Number of bathrooms
    ### Response
    - `prediction`: float, at random

    """
    prediction = predict_price(listing)

    return prediction
