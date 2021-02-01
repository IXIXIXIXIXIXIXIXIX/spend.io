
from flask import Flask, render_template, request, redirect, Blueprint
from app.models.user_assets import current_user
from app.models.view_filter import ViewFilter
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository



viewfilters_blueprint = Blueprint("viewfilters", __name__)

@viewfilters_blueprint.route("/viewfilters/addtag", methods=['POST'])
def addtag():

    tag = tag_repository.select(request.form['filter_tag_choice']) 

    current_user.view_filter.add_tag(tag)

    return redirect(request.referrer)