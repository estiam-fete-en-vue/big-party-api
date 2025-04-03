from fastapi import HTTPException
from supabase import create_client, Client
import os
from dotenv import load_dotenv
load_dotenv()

url:str = os.environ.get("SUPABASE_URL")
key:str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def checkAuth():
  if (supabase.auth.get_session() is None):
    raise HTTPException(status_code=401, detail='User not authenticated')