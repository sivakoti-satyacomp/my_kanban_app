from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() #Instance of SQLAlchemy

class User_Info(db.Model):
    __tablename__="user_info"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String,nullable=False)
    full_name=db.Column(db.String,nullable=False)
    user_name=db.Column(db.String,unique=True,nullable=False)
    pwd=db.Column(db.String,nullable=False)
    role=db.Column(db.Integer,nullable=False,default=1)
    lists=db.relationship("Lists",backref="user_info")


class Lists(db.Model):
    __tablename__="lists"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey("user_info.id"),nullable=False)
    cards=db.relationship("Cards",backref="lists")
    

class Cards(db.Model):
    __tablename__="cards"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    content=db.Column(db.String,nullable=False)
    created_dt=db.Column(db.String,nullable=False)
    last_updated_dt=db.Column(db.String,nullable=False)
    dead_line=db.Column(db.String,nullable=False)
    status=db.Column(db.Integer,nullable=False,default=0)
    list_id=db.Column(db.Integer,db.ForeignKey("lists.id"),nullable=False)

