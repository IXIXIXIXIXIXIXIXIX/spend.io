
from flask import Flask, render_template, request, redirect, Blueprint
import decimal
import app.repositories.user_repository as user_repository
from app.models.user_assets import current_user


users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/user/edit",methods=['post'])
def change_budget():
    
    amount = request.form['amount']

    current_user.change_budget(decimal.Decimal(amount))

    return redirect(request.referrer)
