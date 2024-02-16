from flask import Blueprint
from .models import Client, Chambre, Reservation
from .database import db
from flask import request, jsonify
from datetime import datetime

main = Blueprint("main", __name__)


@main.route("/api/chambres/disponibiles", methods=["GET"])
# renvoie les chambres disponibles pour les dates spécifiées
def chambres_disponibles():
    data = request.get_json()
    date_arrivee = datetime.strptime(data["date_arrivee"], "%Y-%m-%d")
    date_depart = datetime.strptime(data["date_depart"], "%Y-%m-%d")

    # Recherche des chambres disponibles pour les dates spécifiées
    chambres_disponibles = (
        db.session.query(Chambre)
        .filter(
            ~Chambre.reservations.any(
                (Reservation.date_arrivee <= date_depart)
                & (Reservation.date_depart >= date_arrivee)
            )
        )
        .all()
    )

    json_chambres_disponibles = [
        {
            "id": chambre.id,
            "numero": chambre.numero,
            "type": chambre.type,
            "prix": chambre.prix,
        }
        for chambre in chambres_disponibles
    ]

    return jsonify(json_chambres_disponibles)


@main.route("/api/reservations", methods=["POST"])
# ajoute une réservation
def ajouter_reservation():
    data = request.get_json()

    data["date_arrivee"] = datetime.strptime(data["date_arrivee"], "%Y-%m-%d")
    data["date_depart"] = datetime.strptime(data["date_depart"], "%Y-%m-%d")

    verification_reservation_chambre = Reservation.query.filter(
        (Reservation.id_chambre == data["id_chambre"])
        & (Reservation.date_arrivee <= data["date_depart"])
        & (Reservation.date_depart >= data["date_arrivee"])
    ).all()

    # Vérification de la disponibilité de la chambre
    if verification_reservation_chambre:
        return jsonify(
            {
                "success": False,
                "message": "La chambre est déjà réservée pour ces dates",
            }
        )

    reservation = Reservation(
        id_client=data["id_client"],
        id_chambre=data["id_chambre"],
        date_arrivee=data["date_arrivee"],
        date_depart=data["date_depart"],
    )

    db.session.add(reservation)
    db.session.commit()

    return jsonify({"success": True, "message": "Réservation ajoutée avec succès"})


@main.route("/api/reservations/<int:id>", methods=["DELETE"])
# supprime une réservation
def supprimer_reservation(id):
    reservation = Reservation.query.get(id)

    db.session.delete(reservation)
    db.session.commit()

    return jsonify({"success": True, "message": "Réservation supprimée avec succès"})


@main.route("/api/chambres", methods=["POST"])
# ajoute une chambre
def ajouter_chambre():
    data = request.get_json()

    chambre = Chambre(numero=data["numero"], type=data["type"], prix=data["prix"])

    db.session.add(chambre)
    db.session.commit()

    return jsonify({"success": True, "message": "Chambre ajoutée avec succès"})


@main.route("/api/chambres/<int:id>", methods=["PUT", "DELETE"])
def modifier_chambre(id):
    # modifier une chambre grâce à son id
    if request.method == "PUT":
        data = request.get_json()

        chambre = Chambre.query.get(id)

        chambre.numero = data["numero"]
        chambre.type = data["type"]
        chambre.prix = data["prix"]

        db.session.commit()

        return jsonify({"success": True, "message": "Chambre modifiée avec succès"})

    # supprimer une chambre grâce à son id
    if request.method == "DELETE":
        chambre = Chambre.query.get(id)

        db.session.delete(chambre)
        db.session.commit()

        return jsonify({"success": True, "message": "Chambre supprimée avec succès"})

    return jsonify({"success": False, "message": "Méthode non autorisée"})


@main.route("/api/clients", methods=["POST"])
# ajoute un client
def ajouter_client():
    data = request.get_json()

    client = Client(nom=data["nom"], email=data["email"])

    db.session.add(client)
    db.session.commit()

    return jsonify({"success": True, "message": "Client ajouté avec succès"})
