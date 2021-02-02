from flask import Flask
app = Flask(__name__)
from app.controllers import controller
from app.controllers.transactions_controller import transactions_blueprint
from app.controllers.viewfilters_controller import viewfilters_blueprint
from app.controllers.tags_controller import tags_blueprint
from app.controllers.merchants_controller import merchants_blueprint

app.register_blueprint(transactions_blueprint)
app.register_blueprint(viewfilters_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(merchants_blueprint)