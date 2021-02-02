from flask import Flask, render_template, request, redirect, Blueprint
import app.repositories.user_repository as user_repository
import app.repositories.colour_repository as colour_repository
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository
import app.repositories.transaction_repository as transaction_repository
from app.models.tag import Tag
from app.models.user_assets import current_user

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
# Displays all tags and edit functions

    tags = tag_repository.select_all()
    colours = colour_repository.select_all()

    return render_template("/tags/index.html", tags = tags, colours = colours)


@tags_blueprint.route("/tags/<id>/edit", methods=['post'])
def edit_tag(id):
# Saves changes to tags

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

@tags_blueprint.route("/tags", methods=["post"])
def save_tag():

    colour = colour_repository.select(request.form['new_tag_colour'])
    name = request.form['new_tag_name']

    new_tag = Tag(name, colour) 
    tag_repository.save(new_tag)

    return redirect(request.referrer)