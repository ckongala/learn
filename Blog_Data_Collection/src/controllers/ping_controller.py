from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1/ping/")
async def read_ping():
    return {"message": "Blog Data Collection is working"}
