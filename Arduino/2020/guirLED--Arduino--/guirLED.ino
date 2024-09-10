/*  guirLED
 * --------
 * On stocke le n° des LED dans le tableau niemeLED,
 * Le tableau à 2 dimensions ledON permet d'enregistrer
 * differents schémas possibles d'allumage/ extinction
 * des LED. Pour ledON[x][y]
 * - x correspond à une étape d'allumage/extinction
 * - y correspond aux LED
 * 
 * Ainsi quand ledON[1][4] -> la LED n°10 s'allume !
 * 
 * 
 NB: Etant donné que le montage part de la borne +5V
 pour aller vers les ports correpondants à chaque LED
 (respectivement 2, 4, 6, 8, 10), les LED 
 s'allument quand digitalWrite -> LOW
 et 
 s'eteingnent quand digitalWrite -> HIGH.

 Quand un port envoir du courant, quand la fonction
 digitalWrite est sur HIGH, ce courant s'oppose au courant
 emis par la borne +5V, il n'y a donc pas de diffenrence de
 potentiel => la LED ne s'allume pas
 
 */

int niemeLED[5] = {2, 4, 6, 8, 10};

/*
NB: Etant donné que le montage est à l'envers 
(c'est à dire que les ports font office de bornes 
négatives)
les LED s'allument quand digitalWrite -> LOw
donc quand pour ledON[x][y], y = 0 !
*/
int ledON[7][5] = {
  1, 1, 1, 1, 1,
  1, 1, 1, 1, 0,
  1, 1, 1, 0, 1,
  1, 1, 0, 1, 1,
  1, 0, 1, 1, 1,
  0, 1, 1, 1, 1,
  1, 1, 1, 1, 1};

int ledOFFRtoL[7][5] = {
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 1,
  0, 0, 0, 1, 1,
  0, 0, 1, 1, 1,
  0, 1, 1, 1, 1,
  1, 1, 1, 1, 1,
  0, 0, 0, 0, 0};

int ledOFFLtoR[7][5] = {
  0, 0, 0, 0, 0,
  1, 1, 1, 1, 1,
  1, 1, 1, 1, 0,
  1, 1, 1, 0, 0,
  1, 1, 0, 0, 0,
  1, 0, 0, 0, 0,
  0, 0, 0, 0, 0};
  
int i;
int x; // ligne de ledON (= nieme Configuration)
int y ; // colonne de ledON (= niemeLED)
boolean TEST = false;
boolean REAL = true;

void setup() {
  
  for (i = 0; i < 5 ; i++){
    pinMode(niemeLED[i], OUTPUT);
    digitalWrite(niemeLED[i], HIGH);
  }

}

void loop() {

  if (REAL){
  
    //1ere configuration
    //--> Les LED s'allument de gauche à droite
  
    for (x = 6 ; x > 0 ; x--){
      for (y = 0 ; y < 5 ; y ++){
        digitalWrite(niemeLED[y], ledON[x][y]);
      }
      delay(500);  
    }
  
    //2eme configuration
    //--> Les LED s'allument de droite à gauche
    for (x = 0 ; x < 6 ; x++){
      for (y = 0 ; y < 5 ; y ++){
        digitalWrite(niemeLED[y], ledON[x][y]);
      }
      delay(500);  
    } 

    //3eme configuration
    //--> Les LED s'eteingnent de droite à gauche
    for (x = 0 ; x < 6 ; x++){
      for (y = 0 ; y < 5 ; y ++){
        digitalWrite(niemeLED[y], ledOFFRtoL[x][y]);
      }
      delay(500);  
    } 

    //4eme configuration
    //--> Les LED s'eteingnent de gauche à droite

    for (x = 6 ; x > 0 ; x--){
      for (y = 0 ; y < 5 ; y ++){
        digitalWrite(niemeLED[y], ledOFFLtoR[x][y]);
      }
      delay(500);  
    }
  } //READ

  if (TEST){
    for (i = 0; i < 5 ; i++){
      digitalWrite(niemeLED[i], LOW);
    }
    delay(500);
    
    for (i = 0; i < 5 ; i++){
      digitalWrite(niemeLED[i], HIGH);
    }
    delay(500);
  }
  
} // <--void loop
