from config import GROWW_API_KEY, GROWW_API_SECRET
from growwapi import GrowwAPI
 
api_key = GROWW_API_KEY
secret = GROWW_API_SECRET

def place_order(stock, quantity):
    access_token = GrowwAPI.get_access_token(api_key=api_key, secret=secret)
    # Use access_token to initiate GrowwAPI
    groww = GrowwAPI(access_token)
    place_order_response = groww.place_order(
    trading_symbol=stock,
    quantity=quantity, 
    validity=groww.VALIDITY_DAY,
    exchange=groww.EXCHANGE_NSE,
    segment=groww.SEGMENT_CASH,
    product=groww.PRODUCT_CNC,
    order_type=groww.ORDER_TYPE_LIMIT,
    transaction_type=groww.TRANSACTION_TYPE_BUY,
    price=250,               # Optional: Price of the stock (for Limit orders)
    trigger_price=245,       # Optional: Trigger price (if applicable)
)

