from flask import Flask, render_template, request, redirect
from flask import Blueprint

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    return render_template("transactions/index.html")