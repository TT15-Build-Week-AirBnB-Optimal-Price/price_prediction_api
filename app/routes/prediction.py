"""
Functions to predict the optimal price for an AirBnB listing.
"""

import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Listing(BaseModel):
    """
    Use this data model to parse the Listing information
        into a request body in JSON
    """

    neighborhood: str = Field(..., example='Washington Virginia Vale')
    property_type: str = Field(..., example='Entire guesthouse')
    room_type: str = Field(..., example='Entire home/apt')
    accomodates: int = Field(..., example=2)

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('accomodates')
    def accomodates_must_be_positive(cls, value):
        """Validate that accomodates is a positive number."""
        assert value > 0, f'accomodates == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(listing: Listing):
    """
    Make predictions for AirBnB Optimal Listing Prices 🔮

    ### Request Body
    - `neighborhood`: neighborhood the listing is located
    - `property_type`: The type of property of the listing
    - `room_type`: The type of room of the listing
    - `accomodates`: Number of people the listing accomodates


    ### Response
    - `prediction`: float, at random

    """
    X_new = listing.to_df()
    log.info(X_new)
    y_pred = random.random() / 2 + 0.5
    return {
        'prediction': y_pred
    }
