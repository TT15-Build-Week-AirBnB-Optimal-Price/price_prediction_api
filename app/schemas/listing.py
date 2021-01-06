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

    neighborhood: str = Field(..., example='Washington Virginia Vale')
    property_type: str = Field(..., example='Entire guesthouse')
    room_type: str = Field(..., example='Entire home/apt')
    accommodates: int = Field(..., example=2)

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('accommodates')
    def accommodates_must_be_positive(cls, value):
        """Validate that accommodates is a positive number."""
        assert value > 0, f'accommodates == {value}, must be > 0'
        return value
