from flask import (render_template, redirect, url_for, flash, request, json,
jsonify)

from app.api import bp
from app.api import PiDart

@bp.route("/getPiApproximation/<string:language>/<int:throws>", methods=["GET"])
def getPiApproximation(language, throws):

    if throws <= 10000000:
        if language == "python":
            yo = PiDart.Dart()
            dartsResults = yo.throwWithPython(throws) 
        
        elif language == "c":
            asobi = PiDart.Dart()
            dartsResults = asobi.throwWithC(throws)  
        
        else:
            return "Sorry you took the wrong way ! "

        return jsonify(dartsResults)
    else:
        return jsonify({"Error":
            "Please choose a number of throws lower than 10 Millions"})

