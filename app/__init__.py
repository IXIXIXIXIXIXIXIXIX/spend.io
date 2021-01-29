from flask import Flask
app = Flask(__name__)
from app.controllers import controller
# from controllers.transaction_controller import transactions_blueprint
from app.controllers.transaction_controller import transactions_blueprint

app.register_blueprint(transactions_blueprint)
