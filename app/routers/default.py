from fastapi import APIRouter, HTTPException
from ..supabaseClient import isAuthenticated

router = APIRouter()

@router.get("/test")
async def test():
  return isAuthenticated()

@router.get("*")
async def error_404():
  raise HTTPException(status_code=404, detail='not found')
