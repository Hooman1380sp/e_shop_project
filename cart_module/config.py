
SANDBOX = ''
# ? sandbox merchant
if SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

MERCHANT = ''
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
amount = 1000  # Rial / Required
description = "نهایی کردن خرید از سایت ما"  # Required
phone = ''  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'
