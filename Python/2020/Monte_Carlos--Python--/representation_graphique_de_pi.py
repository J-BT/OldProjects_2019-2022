####################################
########## Exercice 3 ##############
####################################
###### Approximation de pi #########
#### Methode de Monte-Carlo########
####################################


from graphics import *
from random import *


def main():
  
    flechette_dans_cible = 0
    flechette_en_dehors_de_cible = 0
    
    #_______CREATION FENETRE GRAPHIQUE_____________# 
    fenetre = GraphWin("Graphique_de_pi", 1000, 1000)
    fenetre.setBackground("white")
      #---> Si [1/4 DE CERCLE], alors :
    #fenetre.setCoords(-0.05, -0.05, 1.05, 1.05)
      #---> Si [CERCLE ENTIER], alors :
    fenetre.setCoords(-1.25, -2, 1.25, 1.40)
    #Titre
    Text(Point(0,1.25), "Approximation de pi ").draw(fenetre)

    #Input Text "Nombre de lancers"
    Text(Point(-0.75,-1.35), "Combien de lancers ? :").draw(fenetre)
    inputText = Entry(Point(-0.15,-1.35), 10)
    inputText.setText("")
    inputText.draw (fenetre)
    #Output Text "Approximation de pi"
    Text(Point(0.50,-1.35), "Approximation =").draw(fenetre)
    outputText = Text(Point(0.80,-1.47),"")
    outputText.draw (fenetre)
    #Bouton
    button = Text(Point(0,-1.70),"C'EST PARTI !!")
    button.draw(fenetre)
    Rectangle(Point(-0.5, -1.9) ,Point(0.5,-1.5)).draw(fenetre)

    #Carre echelle
    carre_echelle = Rectangle(Point(-1.1, -1.1),  Point(1.1, 1.1))
    carre_echelle.setWidth(2)
    carre_echelle.setOutline("black")
    #on affiche le carre
    carre_echelle.draw(fenetre)
    
    #Abscisses
    Line(Point(-1,-1.1),Point(-1,-1.05)).draw(fenetre)
    Text(Point(-1,-1.17), "-1").draw(fenetre)
    Line(Point(0,-1.1),Point(0,-1.05)).draw(fenetre)
    Text(Point(0,-1.17), "0").draw(fenetre)
    Line(Point(1,-1.1),Point(1,-1.05)).draw(fenetre)
    Text(Point(1,-1.17), "1").draw(fenetre)
    #Ordonnées
    Line(Point(-1.1,-1),Point(-1.15,-1)).draw(fenetre)
    Text(Point(-1.2,-1), "-1").draw(fenetre)
    Line(Point(-1.1,0),Point(-1.15,0)).draw(fenetre)
    Text(Point(-1.2,0), "0").draw(fenetre)
    Line(Point(-1.1,1),Point(-1.15,1)).draw(fenetre)
    Text(Point(-1.2,1), "1").draw(fenetre)
    ##signe perpendiculaire   
    petit_carre = Rectangle(Point(-1.1, -1.1),  Point(-1.04, -1.04))
    petit_carre.setWidth(1.5)
    petit_carre.setOutline("black")
    #on affiche le petit_carre
    petit_carre.draw(fenetre)
    #----------------------------------------------#

    

    #_______________CERCLE_________________________#
    # Creation du cercle
    centre_cercle = Point(0,0)
    cercle = Circle(centre_cercle, 1)
    cercle.setWidth(2)
    cercle.setOutline("blue")
    #on affiche le cercle
    cercle.draw(fenetre)
    #----------------------------------------------#
    
    
    #-______________CARRE _________________________#
    #Creation du carre
    carre = Rectangle(Point(-1, -1),  Point(1, 1))
    carre.setWidth(2)
    carre.setOutline("red")
    
    #on affiche le carre
    carre.draw(fenetre)
    #----------------------------------------------#


    #On attends que l'utilisateur clique pour entrer un nombre de flechette
    fenetre.getMouse()

    #on converrti l'input de l'utilisateur
    nombre_de_lancers_de_flechettes = int(inputText.getText())
    
  
    print("*******************************************")
    print("*************Bienvenue dans****************")
    print("**********Lancer de flechette**************")
    print("*******************************************")
    print("*******************************************")

  

    for i in range (1, nombre_de_lancers_de_flechettes + 1):# 100 sera remplacé par nombre_de_lancers
        #uniform(), renvoie un point au hazard compris entre -1 et 1
        x = uniform(-1,1)
        y = uniform(-1,1)
    
        if x**2 + y**2 <= 1:
            flechette_dans_cible += 1  # On ajoute 1 lancer dans la cible
            #_______________POINT BLEU__________________________#
            #creation d'un point bleu (dans la cible)
            f_de_c = flechette_dans_cible
            f_de_c = Point(x, y)
            f_de_c.setFill("blue")
          
            #on affiche le point
            f_de_c.draw(fenetre)
            #---------------------------------------------------#
        
        else: # donc si (x*x) + (y*y) > 1:
            flechette_en_dehors_de_cible += 1  # On ajoute 1 lancer en dehors de la cible
            
            #_______________POINT ROUGE__________________________#
            #creation d'un point rouge (dans la cible)
            f_e_d_de_c = flechette_en_dehors_de_cible
            f_e_d_de_c = Point(x, y)
            f_e_d_de_c.setFill("red")
          
            #on affiche le point
            f_e_d_de_c.draw(fenetre)
            #----------------------------------------------------#
      
    ratio_cible_touchee = flechette_dans_cible/i

      
    # Car appro de pi = proba dans cercle * 4 
    approximation_de_pi = ratio_cible_touchee * 4
      
      
    print("pour nombre_de_lancer_de_flechettes = ", nombre_de_lancers_de_flechettes )
    print("approximation_de_pi = ", approximation_de_pi) #nombre qui se rapporchera de pi

    #On affiche l'appproximation de pi
    outputText.setText(approximation_de_pi)

    #On transforme le "C'est parti" en Quitter"
    button.setText("Quitter")
    fenetre.getMouse()
    
    #________FERMETURE FENETRE GRAPHIQUE____________#
    fenetre.close()
    #-----------------------------------------------#
main()


