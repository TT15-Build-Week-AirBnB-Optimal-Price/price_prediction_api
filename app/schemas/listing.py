"""
Defines the Listing Class
"""
from pydantic import BaseModel, Field, validator
import pandas as pd


class Listing(BaseModel):
    """
    Use this data model to parse the Listing information
        into a request body in JSON
    """
    review_scores_rating: float = Field(..., example=98.0)
    review_scores_checkin: float = Field(..., example=10.0)
    property_type: str = Field(..., example='Entire Apartment')
    availability_365: int = Field(..., example=125)
    availability_30: int = Field(..., example=0)
    reviews_per_month: float = Field(..., example=1.6)
    first_review: float = Field(..., example=2458683.5)
    minimum_nights: int = Field(..., example=29)
    availability_90: int = Field(..., example=16)
    beds: float = Field(..., example=2.0)
    availability_60: int = Field(..., example=14)
    accommodates: int = Field(..., example=1)
    longitude: float = Field(..., example=-104.96676)
    host_id: int = Field(..., example=24241149)
    latitude: float = Field(..., example=39.74025)
    minimum_nights_avg_ntm: float = Field(..., example=29.0)
    bedrooms: int = Field(..., example=1)
    neighborhood: str = Field(..., example='Skyland')
    number_of_reviews: int = Field(..., example=55)
    num_baths: float = Field(..., example=1.0)
    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])
