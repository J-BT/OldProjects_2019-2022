from flask import (render_template, redirect, url_for, flash, request, json,
jsonify)

from app.main import bp

@bp.route('/')
@bp.route("/Home", methods= ['GET','POST'] )
def accueil():

    return render_template('index.html', title="Main page")
