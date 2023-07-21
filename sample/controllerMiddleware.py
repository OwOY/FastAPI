from fastapi import Request
from fastapi.exceptions import HTTPException


async def reject_no_payload(request:Request):
    payload = await request.json()
    if not payload:
        raise HTTPException(status_code=400, detail='Payload is required')