import json
import os
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, session, url_for

from app.model.products import get_all_products, get_product_by_id

shop_pages = Blueprint("shop", __name__)

ORDERS_DIR = "submitted-orders"


def get_cart():
    return session.get("cart", {})


def save_cart(cart):
    session["cart"] = cart
    session.modified = True


def cart_item_count():
    return sum(get_cart().values())

@shop_pages.route("/")
def index():
    products = get_all_products()
    count = cart_item_count()
    return render_template("index.html", products=products, cart_count=count)


@shop_pages.route("/cart/add-item")
def add_to_cart():
    product_id = request.args.get("id")
    if product_id is None:
        return redirect(url_for("shop.index"))

    product = get_product_by_id(product_id)
    if product is None:
        return redirect(url_for("shop.index"))

    cart = get_cart()
    key = str(product["id"])
    cart[key] = cart.get(key, 0) + 1
    save_cart(cart)
    return redirect(url_for("shop.index"))




@shop_pages.route("/cart/remove-item")
def remove_from_cart():
    product_id = request.args.get("id")
    if product_id is None:
        return redirect(url_for("shop.cart"))

    cart = get_cart()
    key = str(product_id)
    if key in cart:
        del cart[key]
        save_cart(cart)
    return redirect(url_for("shop.cart"))



@shop_pages.route("/cart")
def cart():
    cart_data = get_cart()
    items = []
    total = 0.0
    for pid, qty in cart_data.items():
        product = get_product_by_id(pid)
        if product:
            subtotal = product["price"] * qty
            total += subtotal
            items.append({
                "product": product,
                "quantity": qty,
                "subtotal": subtotal,
            })
    count = cart_item_count()
    return render_template("cart.html", items=items, total=total, cart_count=count)



@shop_pages.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart_data = get_cart()
    items = []
    total = 0.0
    for pid, qty in cart_data.items():
        product = get_product_by_id(pid)
        if product:
            subtotal = product["price"] * qty
            total += subtotal
            items.append({
                "product": product,
                "quantity": qty,
                "subtotal": subtotal,
            })

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()
        payment_method = request.form.get("payment_method", "cash")

        order = {
            "date": datetime.now().isoformat(),
            "customer": {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "address": address,
                "payment_method": payment_method,
            },
            "products": [
                {
                    "id": item["product"]["id"],
                    "name": item["product"]["name"],
                    "quantity": item["quantity"],
                    "unit_price": item["product"]["price"],
                    "subtotal": item["subtotal"],
                }
                for item in items
            ],
            "total": total,
        }

        
        print("\n========== COMANDA NOUA ==========")
        print(json.dumps(order, indent=2, ensure_ascii=False))
        print("===================================\n")

       
        os.makedirs(ORDERS_DIR, exist_ok=True)
        filename = datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".json"
        filepath = os.path.join(ORDERS_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(order, f, indent=2, ensure_ascii=False)

       
        save_cart({})

        return render_template("order_success.html", order=order, cart_count=0)

    count = cart_item_count()
    return render_template("checkout.html", items=items, total=total, cart_count=count)




@shop_pages.route("/contact")
def contact():
    count = cart_item_count()
    return render_template("contact.html", cart_count=count)

@shop_pages.route("/cart/increase-item")
def increase_cart_item():
    product_id = request.args.get("id")
    if product_id:
        cart = get_cart()
        key = str(product_id)
        if key in cart:
            cart[key] += 1
            save_cart(cart)
    return redirect(url_for("shop.cart"))


@shop_pages.route("/cart/decrease-item")
def decrease_cart_item():
    product_id = request.args.get("id")
    if product_id:
        cart = get_cart()
        key = str(product_id)
        if key in cart:
            if cart[key] > 1:
                cart[key] -= 1
            else:
                del cart[key]
            save_cart(cart)
    return redirect(url_for("shop.cart"))