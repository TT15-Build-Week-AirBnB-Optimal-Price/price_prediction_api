"""Database functions"""

import os

from fastapi import APIRouter, Depends
from app.services.database import get_db

router = APIRouter()


@router.get('/info')
async def get_url(connection=Depends(get_db)):
    """Verify we can connect to the database,
    and return the database URL in this format:

    dialect://user:password@host/dbname

    The password will be hidden with ***
    """
    url_without_password = repr(connection.engine.url)
    return {'database_url': url_without_password}
