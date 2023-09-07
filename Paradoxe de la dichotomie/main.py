import math

# Définition des constantes
VITESSE_INITIALE = 10  # m/s
DISTANCE_INITIALE = 100.0  # m

# Fonction pour calculer la distance restante
def distance_restante(distance_initiale, vitesse_initiale, temps):
    """
    Calcule la distance restante entre la pierre et l'arbre en fonction de la distance initiale, de la vitesse initiale et du temps.

    Arguments :
    distance_initiale : La distance initiale entre la pierre et l'arbre (en m).
    vitesse_initiale : La vitesse initiale de la pierre (en m/s).
    temps : Le temps écoulé depuis le lancement de la pierre (en s).

    Retourne :
    La distance restante entre la pierre et l'arbre (en m).
    """

    # Calcul de la distance parcourue par la pierre
    distance_parcourue = vitesse_initiale * temps

    # Retour de la distance restante
    return distance_initiale - distance_parcourue

# Programme principal

# Initialisation des variables
distance_restante_actuelle = DISTANCE_INITIALE
temps = 0

# Boucle de simulation
while distance_restante_actuelle > 0:
    # Calcul de la distance restante
    distance_restante_actuelle = distance_restante(DISTANCE_INITIALE, VITESSE_INITIALE, temps)

    # Affichage de la position de la pierre
    print(f"Temps : {temps} s\tDistance restante : {distance_restante_actuelle} m")

    # Incrémentation du temps
    temps += 0.1

# Affichage du résultat final
print(f"La pierre a atteint l'arbre en {temps} secondes.")
