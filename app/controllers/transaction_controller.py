from flask import Flask, render_template, request, redirect, Blueprint
import app.repositories.user_repository as user_repository
import app.repositories.colour_repository as colour_repository
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository
import app.repositories.transaction_repository as transaction_repository
transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():

    all_transactions = transaction_repository.select_all()
    transactions_list = []

    for transaction in all_transactions:
        transactions_list.append(transaction)


    return render_template("transactions/index.html", transactions = transactions_list)