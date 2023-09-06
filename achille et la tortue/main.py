# Définition des constantes

DISTANCE_TOTALE = 100
VITESSE_ACHILLE = 10
VITESSE_TORTUE = 1

# Initialisation des positions

position_achille = 0
position_tortue = 0

# Boucle de simulation

for i in range(DISTANCE_TOTALE):

    # Avancement d'Achille

    position_achille += VITESSE_ACHILLE

    # Avancement de la Tortue

    position_tortue += VITESSE_TORTUE

    # Affichage des positions

    print("Achille :", position_achille)
    print("Tortue :", position_tortue)

# Vérification du résultat

if position_achille > position_tortue:
    print("Achille a gagné !")
else:
    print("La Tortue a gagné !")
