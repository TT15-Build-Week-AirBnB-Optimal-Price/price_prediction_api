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
    host_id: int = Field(..., example=615)
    last_review: float = Field(..., example=2459141.5)
    minimum_nights: int = Field(..., example=2)
    latitude: float = Field(..., example=39.69753)
    minimum_nights_avg_ntm: float = Field(..., example=1.0)
    first_review: float = Field(..., example=2459141.5)
    bedrooms: int = Field(..., example=1)
    number_of_reviews: int = Field(..., example=79)
    neighborhood: str = Field(..., example='Washington Virginia Vale')
    num_baths: int = Field(..., example=1)
    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])
