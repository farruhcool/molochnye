from django.http import JsonResponse
from .models import *
from django.shortcuts import render
from .forms import CheckoutContactForm
from django.contrib.auth.models import User

def basket_adding(request):
    return_dict=dict()
    session_key = request.session.session_key
    print(request.POST)
    data= request.POST
    produkt_id=data.get('produkt_id')
    nmb= data.get("nmb")
    is_delete=data.get("is_delete")

    if is_delete=='true':
        ProductInBasket.objects.filter(id=produkt_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key,produkt_id=produkt_id,
                                                                     is_active=True, defaults={"nmb":nmb})
        if not created:
            print("not created")
            new_product.nmb +=int(nmb)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    produkty_total_nmb = products_in_basket.count()
    return_dict["produkty_total_nmb"]=produkty_total_nmb

    return_dict["produkty"]=list()

    for item in products_in_basket:
        produkt_dict = dict()
        produkt_dict["id"]=item.id
        produkt_dict["name"]=item.produkt.name
        produkt_dict["price_per_item"]=item.price_per_item
        produkt_dict["nmb"]=item.nmb
        return_dict["produkty"].append(produkt_dict)


    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            name = data.get("name", "5464654")
            phone = data["phone"]
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

            zakaz = Zakaz.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)
            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    print(type(value))

                    product_in_basket.nmb = value
                    product_in_basket.save(force_update=True)


                    ProductInOrder.objects.create(produkt=product_in_basket.produkt, nmb=product_in_basket.nmb,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price= product_in_basket.total_price,
                                                  zakaz=zakaz)

        else:
            print("no")
    return render(request, 'zakazy/checkout.html',locals())
