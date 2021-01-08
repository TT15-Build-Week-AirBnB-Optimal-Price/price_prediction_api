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

    ### Request Body; listed in ascending order of feature importances

    'review_scores_rating': overall host review score
    'review_scores_checkin': host review score for check-in
    'property_type': type of property up for booking
    'availability_365': Is porperty/room available in the next 365 days?
    'availability_30': Is porperty/room available in the next 30 days?
    'reviews_per_month': The number of host reviews received per month
    'first_review': When host received first review, in Julian date
    'minimum_nights': The minimum number of nights a client must stay to book
                      property/room
    'availability_90': Is porperty/room available in the next 90 days?
    'beds': Number of beds in property/room
    'availability_60': Is porperty/room available in the next 60 days?
    'accommodates': number of guests the listing accomodates
    'longitude': the property/room's longitudinal position
    'host_id': the host's ID number
    'latitude': the property/room's longitudinal position
    'minimum_nights_avg_ntm': (not sure) min nights in the next 12 months
    'bedrooms': bedrooms in the property
    'neighborhood': the beighborhood the property/room is in, within Denver
    'number_of_reviews': The number of reviews the host has received
    'num_baths': number of baths in the listing(highest impact feature)

    ### Response
    - `prediction`: float, at random

    """
    prediction = predict_price(listing)

    return prediction
