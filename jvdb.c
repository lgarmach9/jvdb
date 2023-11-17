#include <stdio.h>

int main (){
    FILE *archivo;
    archivo = fopen("base de datos.txt","w");
    char *texto= "JVDB";
    fputs(texto, archivo);
    fclose(archivo);
    return 0;   
}