from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class cuarenta(db.Model):
    #clave primaria, primary key
    rowid=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(200),unique=True,nullable=False)
    peliculas=db.Column(db.String(200),unique=True,nullable=False)
    edad=db.Column(db.Integer)
    numeroPeliculas=db.Column(db.Integer)