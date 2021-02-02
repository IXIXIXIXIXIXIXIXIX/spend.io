from flask import Flask, render_template, request, redirect, Blueprint
import app.repositories.user_repository as user_repository
import app.repositories.colour_repository as colour_repository
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository
import app.repositories.transaction_repository as transaction_repository
from app.models.merchant import Merchant
from app.models.user_assets import current_user

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
# Displays all merchants and edit functions

    merchants = merchant_repository.select_all()
    tags = tag_repository.select_active()

    return render_template("/merchants/index.html", tags = tags, merchants = merchants)


@merchants_blueprint.route("/merchants/<id>/edit", methods=['post'])
def edit_merchant(id):
# Saves changes to merchants

    merchant = merchant_repository.select(id)
    tag = tag_repository.select(request.form['tag_choice'])

    if request.form.get('is_active') == 'is_active':
        merchant.activate()
    else:
        merchant.deactivate()
    
    merchant.change_default(tag)
    merchant_repository.update(merchant)


    # Propagate tag change to all transactions with this merchant
    transactions = transaction_repository.select_by_merchant_id(merchant.id)
    
    for transaction in transactions:
        transaction.to_default_tag()
        transaction_repository.update(transaction)

    return redirect(request.referrer)

@merchants_blueprint.route("/merchants", methods=["post"])
def save_merchant():

    tag = tag_repository.select(request.form['new_default_tag'])
    name = request.form['new_merchant_name']

    new_merchant = Merchant(name, tag)
    merchant_repository.save(new_merchant)

    return redirect(request.referrer)