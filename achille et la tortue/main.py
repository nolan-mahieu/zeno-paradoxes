#Définition des constantes

VITESSE_ACHILLE = 10
VITESSE_TORTUE = 1

#Initialisation des positions 

position_achille = 0
position_tortue = 0

#Boucle de simulation 

for i in range(100):
    #Avancement d'Achille
    position_achille += VITESSE_ACHILLE

    # Avancement de la Tortue
    position_tortue += VITESSE_TORTUE

    #Affichage des positions
    print(f"Itération {i}: Achille est à {position_achille} et la Tortue est à {position_tortue}")

#Affichage du résultat final

print(f"Achille a finalement rattrapé la Tortue à l'itération {i}")