from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/*")
async def error_404():
  raise HTTPException(status_code=404, detail='not found')
