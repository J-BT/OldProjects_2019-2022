void tirage_au_sort (int* pnombre_tire_au_sort,
                    int* pnombre_de_mots_dans_dico)
{
    *pnombre_tire_au_sort = (rand()% (*pnombre_de_mots_dans_dico-1+1))-1;

}
