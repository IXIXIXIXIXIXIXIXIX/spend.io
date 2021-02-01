from flask import Flask, render_template, request, redirect, Blueprint
import app.repositories.user_repository as user_repository
import app.repositories.colour_repository as colour_repository
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository
import app.repositories.transaction_repository as transaction_repository
from app.models.user_assets import current_user

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():

    tag_list = []
    merchant_list = []

    all_transactions = transaction_repository.select_all()
    transactions_list = []

    # Register every transaction in month with user
    for transaction in all_transactions:
        current_user.register_spending(transaction)

        if not (transaction.tag in tag_list):
            tag_list.append(transaction.tag)

        if transaction.merchant not in merchant_list:
            merchant_list.append(transaction.merchant)

        if current_user.view_filter.filter_active: 
            if transaction.tag in current_user.view_filter.visible_tags or transaction.merchant in current_user.view_filter.visible_merchants:
                transactions_list.append(transaction)

        else:
            transactions_list.append(transaction)

    return render_template("transactions/index.html", transactions = transactions_list, tags = tag_list, mechants = merchant_list)


@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):

    transaction = transaction_repository.select(id)
    return render_template("/transactions/edit.html", transaction = transaction, current_user = current_user)

