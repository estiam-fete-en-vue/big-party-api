from fastapi import APIRouter
from fastapi.responses import RedirectResponse
import stripe, os
from dotenv import load_dotenv
load_dotenv()



router = APIRouter(
  prefix="/pay"
)

stripe.api_key = os.environ.get("STRIPE_API_KEY")
stripe.sucess_url= os.environ.get("STRIPE_SUCESS_URL")
stripe.cancel_url= os.environ.get("STRIPE_CANCEL_URL")

@router.get("/create-checkout-session")
async def create_checkout_session():
  session = stripe.checkout.Session.create(
    line_items=[
      {
        "price_data": {
          "currency": "eur",
          "product_data": {
            "name": "Ai previews"
          },
          "unit_amount": 100
        },
        "quantity":50
      }
    ],
    mode="payment",
    success_url=stripe.sucess_url,
    cancel_url=stripe.cancel_url
  )

  return RedirectResponse(session.url, status_code=303)