huitLED:
--------

Ce code permet d'allumer les LED 2, 4, 6, 8, 10, 11, 12 et 13 de l'Arduino UNO
selon 2 schemas differents grâce au tableau ledAllumees[26][8]

En iterant sur ce tableau à l'aide de 2 boucles for imbriquées
on peut créer plusieurs combinaisons :

- En partant de la 1ere ligne
- En partant de la derniere ligne
- etc

NB: Etant donné que le montage est à l'envers
(c'est à dire que les ports font office de bornes
négatives)
les LED s'allument quand digitalWrite -> LOw
donc quand pour tableau2Dim[x][y], y = 0 !
Autrement dit quand il y a une difference de potentiel entre 
le +5V et le port sollicité.
