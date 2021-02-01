
from flask import Flask, render_template, request, redirect, Blueprint
from app.models.user_assets import current_user
from app.models.view_filter import ViewFilter



viewfilters_blueprint = Blueprint("viewfilters", __name__)