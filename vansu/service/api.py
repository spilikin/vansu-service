from fhir.resources.organization import Organization
from fhir.resources.address import Address
from fastapi import APIRouter

from . import __version__

api = APIRouter()

@api.get("/info")
async def root():
    return {"version": __version__}

@api.get("/Organization")
async def get_organization():
    org = Organization()
    org.id = "f001"
    org.active = True
    org.name = "Globex"
    org.address = list()
    address = Address()
    address.country = "Germany"
    org.address.append(address)
    return org.dict()