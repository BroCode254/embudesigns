from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
import json
def render_to_pdf(template_src,context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
def DatacookieCart(request):
    try:
        cart = json.loads(request.COOKIES.get('cart', '{}'))
    except json.JSONDecodeError:
        cart = {}

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = 0 

    print(cart)
    for i in cart:
        try:
            quantity = cart[i]['quantity']
            if quantity is None or not isinstance(quantity, int) or quantity <= 0:
                continue 

            cartItems += quantity
            shipping_cost=Order.shipping_cost
            print(shipping_cost)
            product = products.objects.get(id=i)
            total = product.product_price * quantity 
            order['get_cart_total'] += total
            order['get_cart_items'] += quantity

            item = {
                'product': {
                    'id': product.id,
                    'product_price': product.product_price,
                    'product_description': product.description,
                    'product_name': product.product_name,
                    'image': product.image,
                   
                },
                'get_total': total,
                'quantity': quantity,
            }
            items.append(item)
        except products.DoesNotExist:
            print(f"Product with id {i} does not exist.")
            continue 

    return {'order': order, 'items': items, 'cartItems': cartItems}

def AllcartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer).order_by('-date_ordered').filter(complete=False)
        print(orders)
       
        if orders.exists():
            for i in range(orders.__len__()):
                order = orders[i] 
                items = order.orderitem_set.all()
                cartItems=order.get_cart_items
        else:
            order = None
            items = []
            cartItems=0
    else:
       cookieData=DatacookieCart(request)
       order=cookieData['order']
       items=cookieData['items']
       cartItems=cookieData['cartItems']
    return {'order': order, 'items': items,'cartItems':cartItems}