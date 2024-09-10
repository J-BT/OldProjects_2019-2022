int niemeLED[8]= {2,4,6,8,10,11,12,13};
boolean ledAllumees[26][8]={
  1,1,1,0,0,1,1,1, //0
  1,1,0,0,0,0,1,1, //1
  1,0,0,0,0,0,0,1, //2
  0,0,0,0,0,0,0,0, //3
  1,0,0,0,0,0,0,1, //4
  1,1,0,0,0,0,1,1, //5
  1,1,1,0,0,1,1,1, //6
  1,0,1,0,1,0,1,0, //7
  1,1,0,1,0,1,0,1, //8        //1 = LED Eteinte
  1,1,1,0,1,0,1,0, //9        //0 = LED Allumée
  1,1,1,1,0,1,0,1, //10
  1,1,1,1,1,0,1,0, //11
  1,1,1,1,1,1,0,1, //12
  1,1,1,1,1,1,1,0, //13
  0,1,1,1,1,1,1,1, //14
  1,0,1,1,1,1,1,1, //15
  1,1,0,1,1,1,1,1, //16
  1,1,1,0,1,1,1,1, //17
  1,1,1,1,0,1,1,1, //18
  1,1,1,1,1,0,1,1, //19
  1,1,1,1,1,1,0,1, //20
  1,1,1,1,1,1,1,0, //21
  0,1,1,1,1,1,1,0, //22
  1,0,1,1,1,1,0,1, //23
  1,1,0,1,1,0,1,1, //24
  1,1,1,0,0,1,1,1}; //25
int led;
int rangee;
int boolLED;
boolean TEST = false;
boolean REAL = true;

void setup() {
  for (led = 0; led < 8; led++){
    pinMode(niemeLED[led], OUTPUT);
    digitalWrite(niemeLED[led],HIGH);
  }
}//void setup
/*
NB: Etant donné que le montage part de la borne +5V
 pour aller vers les ports correpondants à chaque LED
 ces dernieres s'allument quand digitalWrite -> LOW
 et 
 s'eteingnent quand digitalWrite -> HIGH.

 Quand un port envoie du courant, quand la fonction
 digitalWrite est sur HIGH, ce courant s'oppose au courant
 emis par la borne +5V, il n'y a donc pas de diffenrence de
 potentiel => la LED ne s'allume pas
*/
void loop() {
  if (REAL){
    //1ere combinaison (ledAllumées haut -> bas)
    for (rangee = 0 ; rangee < 26 ; rangee++){
      for(boolLED = 0 ; boolLED < 8 ; boolLED++){
        digitalWrite(niemeLED[boolLED],
                    ledAllumees[rangee][boolLED]);
      }
      delay(400);
    }

    //2eme combinaison (ledAllumées bas -> haut )
    for (rangee = 25 ; rangee >= 0  ; rangee--){
      for(boolLED = 0 ; boolLED < 8 ; boolLED++){
        digitalWrite(niemeLED[boolLED],
                    ledAllumees[rangee][boolLED]);
      }
      delay(400);
    }
  } //REAL
  
  if (TEST){
    for (led = 0; led < 8 ; led++ ){
      digitalWrite(niemeLED[led],LOW);
    }
    delay(500);
    for (led = 0; led < 8 ; led++ ){
      digitalWrite(niemeLED[led],HIGH);
    }
    delay(500);
    }// TEST
}//void loop
