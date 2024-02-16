# TP-Flask_SQLAlchemy_CARIOU_LEON

Cette application est destinée à la gestion des réservations et des chambres d'un hôtel. Elle permet d'ajouter, de modifier et de supprimer des réservations, des chambres et des clients, ainsi que de vérifier la disponibilité des chambres pour des dates spécifiques.

## Utilisation

### Routes disponibles

- **GET /api/chambres/disponibles** :

  - Renvoie les chambres disponibles pour les dates spécifiées.
  - Paramètres de requête :
    - `date_arrivee` : Date d'arrivée au format "YYYY-MM-DD".
    - `date_depart` : Date de départ au format "YYYY-MM-DD".

- **POST /api/reservations** :

  - Ajoute une réservation.
  - Données requises :
    - `id_client` : ID du client effectuant la réservation.
    - `id_chambre` : ID de la chambre réservée.
    - `date_arrivee` : Date d'arrivée au format "YYYY-MM-DD".
    - `date_depart` : Date de départ au format "YYYY-MM-DD".

- **DELETE /api/reservations/<int:id>** :

  - Supprime une réservation spécifiée par son ID.

- **POST /api/chambres** :

  - Ajoute une nouvelle chambre.
  - Données requises :
    - `numero` : Numéro de la chambre.
    - `type` : Type de chambre.
    - `prix` : Prix de la chambre.

- **PUT /api/chambres/<int:id>** :

  - Modifie une chambre spécifiée par son ID.
  - Données requises :
    - `numero` : Nouveau numéro de la chambre.
    - `type` : Nouveau type de chambre.
    - `prix` : Nouveau prix de la chambre.

- **DELETE /api/chambres/<int:id>** :

  - Supprime une chambre spécifiée par son ID.

- **POST /api/clients** :
  - Ajoute un nouveau client.
  - Données requises :
    - `nom` : Nom du client.
    - `email` : Adresse email du client.

### Auteur:

Cariou Léon
