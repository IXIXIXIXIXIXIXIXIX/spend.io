from flask import Flask, render_template, request, redirect, Blueprint
import decimal
import datetime
import app.repositories.user_repository as user_repository
import app.repositories.colour_repository as colour_repository
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository
import app.repositories.transaction_repository as transaction_repository
from app.models.user_assets import current_user
from app.models.transaction import Transaction

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
# Shows transactions and allows filtering

    current_user.reset_budget()

    visible_total = decimal.Decimal(0.00)
    tag_list = []
    merchant_list = []

    all_transactions = transaction_repository.select_all()
    transactions_list = []

    # Register every active transaction with user
    for transaction in all_transactions:
        current_user.register_spending(transaction)

        if current_user.view_filter.filter_active: 
            if transaction.tag.id in current_user.view_filter.tag_ids or transaction.merchant.id in current_user.view_filter.merchant_ids:
                transactions_list.append(transaction)
                visible_total += transaction.amount
        else:
            transactions_list.append(transaction)
            visible_total += transaction.amount

        if transaction.tag.id not in tag_list:
            tag_list.append(transaction.tag.id)

        if transaction.merchant.id not in merchant_list:
            merchant_list.append(transaction.merchant.id)

    # Get tags and merchants from ids
    tags = []
    merchants = []

    for tag in tag_list:
        if tag not in current_user.view_filter.tag_ids:
            tags.append(tag_repository.select(tag))
    
    for merchant in merchant_list:
        if merchant not in current_user.view_filter.merchant_ids:
            merchants.append(merchant_repository.select(merchant))

    sorted_transactions = sorted(transactions_list, key=lambda transaction: transaction.date, reverse=True)

    return render_template("transactions/index.html", current_user = current_user, visible_total = visible_total, 
        transactions = sorted_transactions, tags = tags, merchants = merchants)


@transactions_blueprint.route("/transactions/<id>/edit", methods=['GET'])
def edit_transaction(id):
# Shows form for editing and deleting individual transaction

    transaction = transaction_repository.select(id)
    tags = tag_repository.select_all()
    return render_template("/transactions/edit.html", transaction = transaction, current_user = current_user, tags = tags)


@transactions_blueprint.route("/transactions/<id>/edit", methods=['POST'])
def update_transaction(id):
# Saves edited transaction

    transaction = transaction_repository.select(id)
    tag = tag_repository.select(request.form['tag_choice'])

    transaction.change_tag(tag)
    transaction_repository.update(transaction)

    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/delete")
def delete_transaction(id):
# Deletes a transaction

    transaction_repository.delete(id)
    return redirect("/transactions")

@transactions_blueprint.route("/transaction/new")
def new_transaction():
# Displays new transaction form

    merchants = merchant_repository.select_active()
    tags = tag_repository.select_active()

    return render_template("/transactions/new.html", merchants = merchants, tags = tags)


@transactions_blueprint.route("/transactions", methods=['post'])
def save_transaction():
# Saves new transaction
    
    merchant = merchant_repository.select(request.form['merchant_id'])
    amount = decimal.Decimal(request.form['amount'])
    date =  request.form['date']
    tag_id = request.form['tag_id']

    if tag_id == "None":
        tag = None
    else:
        tag = tag_repository.select(tag_id)    

    transaction = Transaction(merchant, amount, date, tag)
    transaction_repository.save(transaction)

    return redirect(request.referrer)

@transactions_blueprint.route("/transactions/delete")
def delete_all_transactions():
    current_user.reset_budget()
    transaction_repository.delete_all()

    return redirect(request.referrer)