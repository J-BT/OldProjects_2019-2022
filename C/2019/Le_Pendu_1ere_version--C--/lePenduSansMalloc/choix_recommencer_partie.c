void choix_recommencer_partie(char *prejouer_oui_ou_non)
{

    *prejouer_oui_ou_non = getchar();
    *prejouer_oui_ou_non = toupper(*prejouer_oui_ou_non);

    while (getchar()!= '\n');

}
