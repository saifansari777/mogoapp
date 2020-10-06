from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient  
from bson import ObjectId
from validators_mongo import validator, user_validator

app = Flask(__name__)


client = MongoClient("mongodb+srv://saif:brick@cluster0.j6jw7.mongodb.net/db_name?retryWrites=true&w=majority")

db = client.db_name

if db.new_note:
  pass
else:
  db.create_collection("new_note", validator=validator)

if db.users:
  pass
else:
  db.create_collection("_users", validator=user_validator)

notes = db.new_note
users = db.users

@app.route("/",  methods=["GET", "POST"])
def home(user):
  return render_template("index.html", title="Home", user=user)

@app.route("/<user.username>/notes",  methods=["GET", "POST"])
def notess(user):
	if request.form:
    author = user._id
    title = request.form.get("title")
    note = request.form.get("note")
    notes.insert_one({"title":title, "note":note, "author":author})
    return redirect("/")
	 notes_all = notes.find()

	return render_template("notes.html", notes=notes_all)


@app.route("/signup", methods=["POST"])
def signup():
  username = request.form.get("user")
  email = request.form.get("email")
  password = request.form.get("password")
  users.insert_one({"username":username, "email":email, "password":password})
  msg = "Signed up Successfully please Signin"
  return redirect(url_for("/", messages=msg))

@app.route("/signin", methods=["GET", "POST"])
def signin():
  username = request.form.get("user")
  password = request.form.get("password")
  user = users.find({"username":username})
  print(user[0], user)
  if user[0]:
    if user[0]["password"] == password :
      msg = "Successfully signed in"
      return redirect(url_for("/notes", user=user[0], messages=msg))
    else:
      msg = "Wrong password"
      msg_tag ="danger"
      return redirect(url_for("/", messages=msg))

  else:
      msg = "username does not exists"
      msg_tag = "danger"
      return redirect(url_for("/", messages=msg))



@app.route("/delete",  methods=["POST"])
def delete():
	title = request.form.get("title")
	notes.remove({"title":title})
	return redirect("/notes")


@app.route("/<id>/update", methods=["GET", "POST"])
def update(id):
	
	note =  notes.find({"_id":ObjectId(id)})[0]
	print(note)
	if request.form:
		newtitle = request.form.get("newtitle")
		newnote = request.form.get("newnote")
		notes.update_one({"_id":ObjectId(id)}, {"$set" : {"title":newtitle, "note":newnote} })
		return redirect("/notes")
	return render_template("update.html", note=note)

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)