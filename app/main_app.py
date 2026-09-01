from flask import Flask
from .pages.shop import shop_pages

app = Flask(
    __name__,
    static_folder="../public",
    static_url_path="/static",
    template_folder="../templates",
)
app.secret_key = "gxnMaYjinQ27DeBwgKsDyuDQO_shop"

app.register_blueprint(shop_pages)