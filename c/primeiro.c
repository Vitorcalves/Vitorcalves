#include <stdio.h>
#include <stdlib.h>

int main()
{
    int primeiro, segundo, terceiro, total;
    // Faça um programa que leia 3 números
    // inteiros e exiba o resultado da multiplicação entre eles.
    printf("entre com o primeiro numero\n");
    scanf("i", &primeiro);
    printf("entre com o segundo numero\n");
    scanf("i", &segundo);
    printf("entre com o terceiro numero\n");
    scanf("%i", &terceiro);
    total = primeiro * segundo * terceiro;
    printf("a total dos 3 numeros eh: i",total);
    return 0;
}