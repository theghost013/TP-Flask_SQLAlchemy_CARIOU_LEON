from .database import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property


class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    reservations = db.relationship(
        "Reservation", backref="client", lazy="dynamic", cascade="all, delete"
    )


class Chambre(db.Model):
    __tablename__ = "chambres"
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True, nullable=False)
    type = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Float, nullable=False)
    reservations = db.relationship("Reservation", backref="chambre", lazy="dynamic")


class Reservation(db.Model):
    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key=True)
    id_client = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
    id_chambre = db.Column(db.Integer, db.ForeignKey("chambres.id"), nullable=False)
    date_arrivee = db.Column(db.DateTime, nullable=False)
    date_depart = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(100), nullable=False, default="confirmée")
