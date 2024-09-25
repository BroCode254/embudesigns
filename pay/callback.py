# elapp/views.py
import json
from django.http import JsonResponse
from Shop.models import PaymentTransaction

def process_stk_callback(request):
    stk_callback_response = json.loads(request.body)
    log_file = "Mpesastkresponse.json"
    with open(log_file, "a") as log:
        json.dump(stk_callback_response, log)

    merchant_request_id = stk_callback_response['Body']['stkCallback']['MerchantRequestID']
    checkout_request_id = stk_callback_response['Body']['stkCallback']['CheckoutRequestID']
    result_code = stk_callback_response['Body']['stkCallback']['ResultCode']
    result_desc = stk_callback_response['Body']['stkCallback']['ResultDesc']
    amount = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
    transaction_id = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
    user_phone_number = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

    if result_code == 0:
        try:
            transaction=PaymentTransaction.objects.create(
                        merchant_request_id=merchant_request_id,
                        checkout_request_id=checkout_request_id,
                        result_code=0,
                        result_desc=result_desc,
                        amount=amount,  # Initial amount is 0, will be updated in the callback
                        transaction_id=transaction_id,
                        user_phone_number=user_phone_number,
                        expected_amount=amount)
            transaction.save()
            return JsonResponse({'status': 'Transaction successful and amounts match'})

        except PaymentTransaction.DoesNotExist:
            return JsonResponse({'error': 'Transaction does not exist'}, status=404)

    else:
        return JsonResponse({'status': 'Transaction failed', 'result_desc': result_desc}, status=400)
