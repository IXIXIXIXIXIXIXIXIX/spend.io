from flask import Flask, render_template, request, redirect, Blueprint
import app.repositories.user_repository as user_repository
import app.repositories.colour_repository as colour_repository
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository
import app.repositories.transaction_repository as transaction_repository
from app.models.user_assets import current_user

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():

    tags = tag_repository.select_all()
    colours = colour_repository.select_all()

    return render_template("/tags/index.html", tags = tags, colours = colours)


@tags_blueprint.route("/tags/<id>/edit", methods=['post'])
def edit_tag(id):

    tag = tag_repository.select(int(id))
    colour = colour_repository.select(int(request.form['colour_choice']))


    if not tag.reserved:

        if request.form.get('is_active') == 'is_active':
            tag.activate()
        else:
            tag.deactivate()
    
    tag.change_colour(colour)
    tag_repository.update(tag)

    return redirect(request.referrer)