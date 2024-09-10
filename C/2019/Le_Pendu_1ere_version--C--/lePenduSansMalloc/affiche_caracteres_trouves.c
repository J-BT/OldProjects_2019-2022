void affiche_caracteres_trouves (int* ptaille_mot_secret,
                                char* pcaractere_joueur,
                                char pmot_secret[],
                                char pmot_cache[])
{
    for (int i = 0;i<*ptaille_mot_secret;i++)
    {
       if(*pcaractere_joueur == pmot_secret[i])
        {
            pmot_cache[i]=*pcaractere_joueur;
        }
    }
}
