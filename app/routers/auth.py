from fastapi import APIRouter, Response
from  ..supabaseClient import supabase, checkAuth
from ..models import auth

router = APIRouter(
  prefix="/auth"
)

@router.post("/signup", status_code=201)
async def sign_up(credentials:auth.Credentials, response:Response):
  try:
    response.body = supabase.auth.sign_up(
      {
        "email": credentials.email,
        "password": credentials.password
      }
    )
  except Exception as e:
    response.status_code = e.status
    response.body = e
  return response.body

@router.post("/login")
async def sign_in(credentials:auth.Credentials, response:Response):
  try:
    response.body = supabase.auth.sign_in_with_password(
      {
        "email": credentials.email,
        "password": credentials.password
      }
    )
  except Exception as e:
    response.status_code = e.status
    response.body = e
  return response.body

@router.post("/logout")
async def sign_out():
  return supabase.auth.sign_out()

@router.get("/me")
async def user_info(response:Response):
  checkAuth()
  supabase.auth.get_user()