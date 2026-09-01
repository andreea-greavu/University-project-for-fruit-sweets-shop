Fruit Sweets 🍓
For this assignment I built an online shop with fruit and various sweets. I have a main page with images, descriptions and prices for products, buttons to add and remove products from the cart, the shopping cart, an order page with a form and order saving, an order confirmation page, and a contact page.
##Assignment contents:
#app:
main_app.py — initializes the Flask instance and registers the routes
products.py — the product list
shop.py — the app's routes: main page, cart, checkout, contact
#public: product images, Bootstrap files and the CSS
style.css — the CSS styles
images — the product images
bootstrap — Bootstrap files taken from lab 4
#submitted-orders: the folder where orders are automatically saved, each as a json file
#templates: the HTML templates
_layout.html — the base HTML structure used by all pages
cart.html — the cart page
checkout.html — the order form
contact.html — the contact page
index.html — the products page
order_success.html — the confirmation page after placing an order
server.py — starts the Flask server on port 5000
Dockerfile — starts the Flask server in an Alpine container, accessible on port 5000, based on the one from lab 4
requirements.txt — the list of Python dependencies, based on the one from lab 4
I personalized the site with a pink color scheme, and the order confirmation page includes details about the placed order such as the products, each product's price, the total price, buttons to increase or decrease a product's quantity, and saving orders in json format.
To run it, both python3 server.py and docker build -t iap1-tema ./  docker run -p 5000:5000 -it iap1-tema work.
