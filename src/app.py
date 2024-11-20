
from config import app
from flask import redirect, render_template, request, jsonify, flash

from repositories.reference_repository import get_reference, create_reference, delete_all

@app.route("/", methods =["GET", "POST"])
def load_index():    
    # reference = get_reference()
    return render_template("index.html")

@app.route("/get_reference", methods =["GET", "POST"])
def reference_fetcher():
    references = get_reference()
    print(references)
    return render_template("references.html", references=references)

@app.route("/create_reference", methods = ["POST"])
def reference_creation():
    ref_dict = {}
    ref_dict["sitaatin_tunniste"] = request.form.get("sitaatin_tunniste")
    ref_dict["kirjoittajat"] = request.form.get("kirjoittajat")
    ref_dict["otsikko"] = request.form.get("otsikko")
    ref_dict["julkaisu"] = request.form.get("julkaisu")
    ref_dict["vuosi"] = request.form.get("vuosi")
    if request.form.get("julkaisunumero") == "":
        ref_dict["julkaisunumero"] = None
    else:
        ref_dict["julkaisunumero"] = request.form.get("julkaisunumero")
    if request.form.get("sivut") == "":
        ref_dict["sivut"] = None
    else:
        ref_dict["sivut"] = request.form.get("sivut")
    if request.form.get("DOI") == "":
        ref_dict["doi"] = None
    else:
        ref_dict["doi"] = request.form.get("DOI")
    # return kirjoittajat, otsikko, julkaisu, DOI
    print(ref_dict)

    # TODO
    # reference_repository.py funktio joka postaa tietokantaan. 
    create_reference(ref_dict)
    # luo logiikka, tällä hetkellä create_reference funktio pass

    return redirect("/")

@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    delete_all()
    return "Reset"
