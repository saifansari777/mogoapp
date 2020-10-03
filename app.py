from flask import Flask, request, render_template, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient  
from bson import ObjectId
from validators_mongo import validator
from mongoengine import *
app = Flask(__name__)


client = MongoClient("mongodb://127.0.0.1:27017")

db = client.mymongodb

db.create_collection("newnotes", validator=validator)
notes = db.newnotes



@app.route("/",  methods=["GET", "POST"])
def home_page():
	if request.form:
		title = request.form.get("title")
		note = request.form.get("note")
		notes.insert_one({"title":title, "note":note})
		return redirect("/")
	notes_all = notes.find()

	return render_template("home.html", notes=notes_all)

@app.route("/delete",  methods=["POST"])
def delete():
	title = request.form.get("title")
	note = notes.remove({"title":title})
	return redirect("/")


@app.route("/<id>/update", methods=["GET", "POST"])
def update(id):
	
	note =  notes.find({"_id":ObjectId(id)})
	print(note)
	if request.form:
		newtitle = request.form.get("newtitle")
		newnote = request.form.get("newnote")
		notes.update_one({"_id":ObjectId(id)}, {"$set" : {"title":newtitle, "note":newnote} })
		print(notes.update_one({"_id":ObjectId(id)}, {"$set" : {"title":newtitle, "note":newnote} }).modified_count)
		return redirect("/")
	return render_template("update.html", note=note)

if __name__ == '__main__':
	app.run()