from app import app
from flask import render_template,jsonify,request,url_for
from app.models import Session
from app import db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=="POST":
        title = request.form['title']
        video_link = request.form['video_link']
        notes_link = request.form['notes_link']
        new_session = Session(title=title,video_link=video_link,notes_link=notes_link)
        db.session.add(new_session)
        db.session.commit()

    return render_template("add.html")

@app.route("/get",methods=['POST'])
def get():
    if request.method=="POST":
        s = Session.query.get(request.form['code'])
        if s:
            return jsonify({"status":"1","title":str(s.title),"video":str(s.video_link),"file":str(s.notes_link)})
        else:
            return jsonify({"status":"0"})

