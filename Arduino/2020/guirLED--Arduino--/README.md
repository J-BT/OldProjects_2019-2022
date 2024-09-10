guirLED:
-------

Ce code permet d'allumer les LED 2, 4, 6, 8 et 10 de l'Arduino UNO
selon 4 schemas differents :

1) Les LED s'allument de gauche à droite
2) Les LED s'allument de droite à gauche
3) Les LED s'eteingnent de droite à gauche (voir photo)
4) Les LED s'eteingnent de gauche à droite

Pour cela nous avons stocké les differentes combinaisons possibles
dans des tableaux à 2 dimensions, où chaque ligne correspond à un schéma,
et chaque colonne à une LED.

NB: Etant donné que le montage est à l'envers 
(c'est à dire que les ports font office de bornes 
négatives)
les LED s'allument quand digitalWrite -> LOw
donc quand pour tableau2Dim[x][y], y = 0 !
