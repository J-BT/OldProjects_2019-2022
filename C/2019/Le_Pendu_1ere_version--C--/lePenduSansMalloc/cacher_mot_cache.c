void cacher_mot_cache (int* ptaille_mot_secret, char pmot_cache[])
{
   for (int i = 0; i<*ptaille_mot_secret; i++)
    {
        pmot_cache[i]='*';
    }
}
