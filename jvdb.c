#include <stdio.h>
#include <string.h>

int main (int argc, char *argv[]){
    FILE *archivo;
    archivo = fopen("base de datos.txt","a");
    char *texto= argv[1];
    fputs(strcat(texto, "\n"), archivo);
    fclose(archivo);
    return 0;   
}