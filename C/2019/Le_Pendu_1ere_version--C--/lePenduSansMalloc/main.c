#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <ctype.h>
#include <string.h>
#include "cacher_mot_cache.h"
#include "lire_caractere_joueur.h"
#include "affiche_caracteres_trouves.h"
#include "dessin_du_pendu.h"
#include "choix_recommencer_partie.h"
#include "nombre_tire_au_sort.h"

#define TAILLE_MAX_MOT 100  ///<= **** REPLACER PAR MALLOC OU CALLOC ******
#define NOMBRE_ESSAIS_MAX 10

int main (int argc, char* argv[])

{
    srand(time(NULL));
    int commencer_partie = 1;

    while(commencer_partie)
    {
        char mot_secret [TAILLE_MAX_MOT] = "";
        char mot_cache [TAILLE_MAX_MOT] = "";
        char copie_mot_cache [TAILLE_MAX_MOT] = "";
        char lettres_tapees [11] = "";
        char caractere_joueur = 0;
        char rejouer_oui_ou_non = 0;
        int caractere_actuel = 0;
        int nombre_de_mots_dans_dico = 0;
        int compteur_tours_moins_un = 0;
        int nombre_essai_restant = 0;
        int taille_mot_secret = 0;
        int nombre_tire_au_sort = 0;

        /*------------------------- DICTIONNAIRE ---------------------------*/

        FILE* dico = NULL;
        //Ouverture du fichier dicitonnaire.txt en mode lecture
        dico = fopen("dictionnaire.txt", "r");

        //On verifie si ouverture du fichier possible
        if(dico != NULL)
        {
            do
            {
                //Curseur virtuel balaye le fichier dico pour le lire
                caractere_actuel = fgetc(dico);
                if(caractere_actuel == '\n')
                {
                    //Ajoute +1 à nombre_de_mots_dans_dico
                    // si rencontre un espace
                    nombre_de_mots_dans_dico ++;
                }
            } while (caractere_actuel != EOF);

            //Pr remetttre curseur de fgets au debut du fichier dico
            rewind(dico);

            //Nombre compris entre 1 et nombre_de_mots_dans_dico
            tirage_au_sort (&nombre_tire_au_sort,
                            &nombre_de_mots_dans_dico);
            printf("Mot secret: %d/%d\n\n",nombre_tire_au_sort,
                    nombre_de_mots_dans_dico);


            for(int i = 0; i<nombre_tire_au_sort; i++)
            {
                //On met Nième mot tiré au sort dans mot_secret
                fgets(mot_secret, TAILLE_MAX_MOT, dico);
            }
            //On retire l'espace (\n) dans mot_secret
            // (~> mot_secret[espace] = 0)
            mot_secret[strlen(mot_secret)-1] = 0 ;

        //On ferme le fichier dictionnaire.txt
        fclose(dico);
        }
        else
        {
            printf("\aOuverture du fichier dictionnaire.txt impossible!\n\n");
        }

        /*--------INITIALISATION APRES FERMETURE DU DICTIONNAIRE------------*/

        nombre_essai_restant = NOMBRE_ESSAIS_MAX;
        // On calcule la taille de mot_secret
        taille_mot_secret = strlen(mot_secret);
        // On copie mot_secret dans mot caché
        strcpy(mot_cache, mot_secret);
        // On remplace les lettres de mot_caché par des *
        cacher_mot_cache (&taille_mot_secret, &mot_cache);

        /*-------------------------- DEBUT DU JEU --------------------------*/

        // Le #define est situé dans dessin_du_pendu
        BIENVENUE()

        while(nombre_essai_restant>0)
        {
            // Le pendu commence à se dessiner si joueur perd un essai
            if (nombre_essai_restant == 9)
            {
                PENDU_9()
            }
            if (nombre_essai_restant == 8)
            {
                PENDU_8()
            }
            if (nombre_essai_restant == 7)
            {
                PENDU_7()
            }
            if (nombre_essai_restant == 6)
            {
                PENDU_6()
            }
            if (nombre_essai_restant == 5)
            {
                PENDU_5()
            }
            if (nombre_essai_restant == 4)
            {
                PENDU_4()
            }
            if (nombre_essai_restant == 3)
            {
                PENDU_3()
            }
            if (nombre_essai_restant == 2)
            {
                PENDU_2()
            }
            if (nombre_essai_restant == 1)
            {
                PENDU_1()
            }
            strcpy(copie_mot_cache, mot_cache);

            printf("Choisissez une lettre  %s\t\t\t\t\t \
                    Nombre d'essais restant : %d\n",
                    mot_cache,
                    nombre_essai_restant);
            if(nombre_essai_restant<10)
            {
                // Ne s'affichent qu'au 2eme tour
                printf("-> Vous avez entre : %s\n\n", lettres_tapees);
            }
            //On lit la lettre saisie par le joueur,
            // puis on la stocke ds caractere_joueur
            lire_caractere_joueur (&caractere_joueur);


            compteur_tours_moins_un = NOMBRE_ESSAIS_MAX - nombre_essai_restant;
            //On affecte les lettres entrees par joueur dans lettres_tapees
            lettres_tapees[compteur_tours_moins_un] = caractere_joueur;


            /*"mot_cache "sera modifié avec la fonction suivante
            On devoile le/les caracteres saisis par le joueur si corrects*/
            affiche_caracteres_trouves (&taille_mot_secret,
                                        &caractere_joueur,
                                        &mot_secret,
                                        &mot_cache);

            // Si copie_mot_cache et mot_cache sont identiques
            if (strcmp(copie_mot_cache, mot_cache)== 0)
            {
                printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
                        \n\n\n\n\n\n\t\t\t\t\t Dommage, essayez encore !\n\n");
            }
            // Si copie_mot_cache et mot_cache sont differents
            else if (strcmp(copie_mot_cache, mot_cache)!= 0)
            {
                // Si le joueur trouve une lettre
                printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
                        \n\n\n\n\n\n\t\t\t\t\t Nice!!\n\n");

                //On empeche le joueur d'avoir un essai en -
                nombre_essai_restant++;
            }
            //On sort de la boucle si mot_secret = mot_caché
            if(strcmp(mot_secret, mot_cache)== 0)
            {
                nombre_essai_restant = 0;
            }
            nombre_essai_restant--;

        }
    /*------------------------------ RESULTAT ------------------------------*/
        // Si le joueur a trouvé le mot secret
        if(strcmp(mot_secret, mot_cache)== 0)
        {
            printf("********************************************\n");
            printf("**** Felicitations!! Vous avez gagne!!! ****\n");
            printf("********************************************\t\t\t\
                    -------------------------------------\n");
            printf("\t\t\t\t\t\t\t\t---  Le mot secret etait: %s ---\n",
                    mot_secret);
            printf("                                            \
                    \t\t\t-------------------------------------\n\n");
        }
        //Si le joueur a perdu
        else
        {
            PENDU_0()
            printf("********************************************\n");
            printf("******* Dommage!!! Vous avez perdu!!! ******\n");
            printf("********************************************\n");
            printf("---  Le mot secret etait: %s ---\n\n",
                    mot_secret);

        }
    /*---------------------- CHOIX NOUVELLE PARTIE -------------------------*/

        //On affecte 2 à commencer_partie pour enfermer le joueur
        // ds boucle, ci dessous, tant que pas 'O' ou 'N'
        commencer_partie = 2;

        while (commencer_partie == 2)
        {
            printf("Voulez vous rejouer ?\n");
            printf("|-----------------------------------------------------|\n");
            printf("| Entrez 'O' pour OUI|\t\t|Entrez 'N' pour NON ?|\n");
            printf("|-----------------------------------------------------|\n");
            choix_recommencer_partie(&rejouer_oui_ou_non);

            if(rejouer_oui_ou_non == 'O')
            {
                commencer_partie = 1;
            }
            else if (rejouer_oui_ou_non == 'N')
            {
                commencer_partie = 0;
            }
        }
        ESPACE_POUR_NOUVELLE_PARTIE()
    }

    return 0;
}
