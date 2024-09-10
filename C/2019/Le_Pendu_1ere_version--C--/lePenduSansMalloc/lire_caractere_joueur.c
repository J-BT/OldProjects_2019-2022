void lire_caractere_joueur (char* pcaractere_joueur)
{
    *pcaractere_joueur = getchar();
    *pcaractere_joueur = toupper(*pcaractere_joueur);

    while(getchar() != '\n');

}
