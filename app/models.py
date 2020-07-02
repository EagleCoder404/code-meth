from app import db
import uuid

def rca():
    
    test = str(uuid.uuid4().hex[:6].upper())
    while Session.query.get(test):
        test = str(uuid.uuid4().hex[:6].upper())
    return test

class Session(db.Model):
    id =         db.Column(db.String,primary_key=True,default=rca)
    title =      db.Column(db.String(200),nullable=False)
    video_link = db.Column(db.String,nullable=False)
    notes_link = db.Column(db.String,nullable=False)

    def __repr__(self):
        return "%r -- %r"%(self.id,self.title)