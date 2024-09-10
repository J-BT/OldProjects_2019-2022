# include <stdio.h>
# include <stdlib.h>
# include <time.h>
# include <string.h>

/*
    ----- TO CALL C FUNCTION IN .PY FILE ----------
    cc -fPIC -shared -o dataForPythonFile.so dataForPythonFile.c

    -> This with create a .so file in the working directory 
    callable in python file through ctypes library

    ------- TO EXECUTE C FILE ON LINUX ------------
    for execute a c programm with linux:
    1) gcc dataForPythonFile.c  : this command will create a a.out file
    2) ./a.out       : the read the fil created

*/

char* getJsonForPython(int maxThrows);


int main(int argc, char *argv[]){
    
    //throwWithC(500);
    //printf("%s\n", getJsonForPython(100));

    //printf("%s\n ",getJsonForPython(100));
    getJsonForPython(100);

    return 0;
}

char* getJsonForPython(int maxThrows) {

    float randomX = 0.0;
    float randomY = 0.0;
    float positiveOrNegative = 0.0;
    int throwsInsideTarget = 0;
    int throwsOutsideTarget = 0;
    float successRatio = 0.0;
    float piApproximation = 0.0;
    int totalThrows = 0;

    /*
        create a function to inverse sign of a float at random
        given float * 1 or given float * (-1)
    */

    srand((float)time(NULL));

    for (int throw = 1 ; throw <  maxThrows + 1; throw++){
        totalThrows+=1;
        //Random between 1 and 0
        positiveOrNegative = (float)(rand() % 2 + (-1));
        //If positiveOrNegative == 0 , we change it to 1
        if (positiveOrNegative == 0.000000){
            positiveOrNegative = 1.000000;
        }

        //Let's generate random coordinate x
        randomX =(float)rand()/(float)(RAND_MAX) * 1;
        // random positive or negative
        randomX = randomX * positiveOrNegative;


        //Random between 1 and 0
        positiveOrNegative = (float)(rand() % 2 + (-1));
        //If positiveOrNegative == 0 , we change it to 1
        if (positiveOrNegative == 0.000000){
            positiveOrNegative = 1.000000;
        }
        //And now a random coordinate y
        randomY =(float)rand()/(float)(RAND_MAX) * 1;
        // random positive or negative
        randomY = randomY * positiveOrNegative;
            

        if ((randomX*randomX) + (randomY*randomY) <= 1){
            throwsInsideTarget += 1;
        }
        else if ((randomX*randomX) + (randomY*randomY) > 1){
            throwsOutsideTarget += 1;
        }
            
        else{
            printf("Throw : %d = Something's wrong...This is odd", throw);
        }
            
        
    }
    successRatio = ((float)throwsInsideTarget / (float)totalThrows);
    piApproximation = ((float)successRatio * 4);

    /*
    printf("Total throws : %d \n", totalThrows);
    printf("Throws inside : %d, Throws outside : %d\n",
        throwsInsideTarget, throwsOutsideTarget);
    printf("Success ratio : %f, Pi Approximation : %f\n",
    successRatio, piApproximation);
    */

    char jsonForPython[100]  = "'totalThrows' : ";
    char str2[20] = "";
    sprintf(str2, "%d, ", totalThrows);

    char str3[100] = "'throwsInside' : ";
    char str4[20] = "";
    sprintf(str4, "%d, ", throwsInsideTarget);
    
    char str5[100] = "'throwsOutside' : ";
    char str6[20] = "";
    sprintf(str6, "%d, ", throwsOutsideTarget);
    
    char str7[100]  = "'successRatio' : ";
    char str8[20] = "";
    sprintf(str8, "%f, ", successRatio);
    
    char str9[100]  = "'piApproximation' : ";
    char str10[20] = "";
    sprintf(str10, "%f", piApproximation);
    char str11[100]  = "";

    strcat(jsonForPython,str2);
    strcat(jsonForPython,str3); 
    strcat(jsonForPython,str4);
    strcat(jsonForPython,str5);
    strcat(jsonForPython,str6);
    strcat(jsonForPython,str7); 
    strcat(jsonForPython,str8);
    strcat(jsonForPython,str9);
    strcat(jsonForPython,str10);

    //printf("%s\n ",strcat(jsonForPython,str11));

    /*
        Let's write in jsonToExtractFromC.txt
        the string to be retreived in python file
    */
    FILE *fp;
   fp = fopen("jsonToExtractFromC.txt", "w+");
   fputs(strcat(jsonForPython,str11), fp);
   fclose(fp);
    
    return strcat(jsonForPython,str11);
                                 
}
