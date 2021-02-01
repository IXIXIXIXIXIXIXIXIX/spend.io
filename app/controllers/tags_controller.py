from flask import Flask, render_template, request, redirect, Blueprint
import app.repositories.user_repository as user_repository
import app.repositories.colour_repository as colour_repository
import app.repositories.tag_repository as tag_repository
import app.repositories.merchant_repository as merchant_repository
import app.repositories.transaction_repository as transaction_repository
from app.models.user_assets import current_user

tags_blueprint = Blueprint("tags", __name__)