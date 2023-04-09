from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
  id = db.column(db.Integer,primary_key=True)
  email = db.Column(db.String(150), unique=True,unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  dept_name = db.Column(db.String(150))
  teachers = db.relationship('Teacher')




class Teacher(db.Model):
  id = db.column(db.Integer,primary_key=True)
  email = db.Column(db.String(150), unique=True,unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  last_name = db.Column(db.String(150))
  dept = db.Column(db.String(150))
  user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
  