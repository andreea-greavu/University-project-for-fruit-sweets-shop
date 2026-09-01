
PRODUCTS = [
    {
        "id": 1,
        "name": "Akai CRUNCKHY",
        "description": "Acai, budincă de chia, granola, căpșuni, afine și toppinguri din boabe de cacao.",
        "price": 49.99,
        "image": "/static/images/poza1.jpg",
        "category": "Akai",
    },
    {
        "id": 2,
        "name": "Akai FRUITY",
        "description": "Acai, porție dublă de granola, banană, căpșuni, fructul pasiunii.",
        "price": 49.99,
        "image": "/static/images/poza2.jpg",
        "category": "Akai",
    },
    {
        "id": 3,
        "name": "Akai ALMONDS",
        "description": "Acai, colagen, unt de migdale, migdale, afine, căpșuni",
        "price": 49.99,
        "image": "/static/images/poza3.jpg",
        "category": "Akai",
    },
    {
        "id": 4,
        "name": "Akai Matcha",
        "description": "Acai, budincă de chia cu matcha dublă, căpșuni, fructe goji, miere",
        "price": 49.99,
        "image": "/static/images/poza4.jpg",
        "category": "Akai",
    },
    {
        "id": 5,
        "name": " Cotton Candy with Courvoisier VSOP & matcha ice cream  ",
        "description": "Faină, ouă, lapte, zahăr, extract de vanille, esență de portocală, cremă de vanilie, înghețată matcha, vată de zahar, coniac, fructe de pădure",
        "price": 39.99,
        "image": "/static/images/poza5.jpg",
        "category": "Dulciuri",
    },
    {
        "id": 6,
        "name": "Salted Red Velvet",
        "description": "Făină, ouă, lapte, zahăr, extract de vanilie, esentă de portocală, frișcă, zmeura, mascarpone, crema de branză + BLAT RED VELVET",
        "price": 34.99,
        "image": "/static/images/poza6.jpg",
        "category": "Dulciuri",
    },
    {
        "id": 7,
        "name": "Cinnamon Roll",
        "description": "Făină, ouă, lapte, zahăr, extract de vanilie, esență de portocală, frișcă, scortisoara, fulgi migdale, cocos, fructe padure proaspete, biscuiti",
        "price": 34.99,
        "image": "/static/images/poza7.jpg",
        "category": "Dulciuri",
    },
    {
        "id": 8,
        "name": "Pancakes",
        "description": "Făină, ouă, lapte, zahăr, extract de vanilie,scortisoara, fulgi migdale, cicocolata, biscuiti",
        "price": 31.99,
        "image": "/static/images/poza8.jpg",
        "category": "Dulciuri",
    },
]


def get_all_products():
    return PRODUCTS


def get_product_by_id(product_id):
    product_id = int(product_id)
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None
