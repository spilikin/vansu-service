from fastapi import APIRouter
from . import __version__

api = APIRouter()

@api.get("/info")
async def root():
    return {"version": __version__}
