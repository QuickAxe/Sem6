// 1 -> high
// 0 -> low

#include <stdio.h>
#include <inttypes.h>

int main()
{
    uint8_t binaryString[100];

    printf("Enter length of sequrnce: ");
    int length;
    scanf("%d", &length);
    printf("\n");

    printf("Enter binary sequence: ");
    
    for(int i=0; i<length; i++)
    {
        scanf("%hhu", &binaryString[i]);
    }
    printf("\n");

    //-------------------------------------- printing encoded outputs -------------------------------------------------

    // NRZ -------------------------
    
    printf(" 5v_");
    for(int i=0; i< length; i++)
    {
        printf("¦    ");
    }
    printf("¦\n    |");

    for(int i=0; i < length; i++)
    {
        
        if(binaryString[i] == 0)
            printf("____|");
        else
            printf("\u203E\u203E\u203E\u203E|");
    }
    printf("\n 0v\u203E");

    for(int i=0; i< length; i++)
    {
        printf("¦    ");
    }
    printf("¦\n");

    printf("\n\n");

    //Manchester -------------------
    
    printf(" 5v_");
    for(int i=0; i< length; i++)
    {
        printf("¦    ");
    }
    printf("¦\n    |");

    for(int i=0; i < length; i++)
    {
        
        if(binaryString[i] == 0)
            printf("__|\u203E\u203E");
        else
            printf("\u203E\u203E|__");
    }
    printf("\n 0v\u203E");

    for(int i=0; i< length; i++)
    {
        printf("¦    ");
    }
    printf("¦\n ");

    printf("\n\n");

    // Diff manchester ----------------

    int flag=1;

    printf(" 5v_");
    for(int i=0; i< length; i++)
    {
        printf("¦    ");
    }
    printf("¦\n    |");

    for(int i=0; i < length; i++)
    {
        
        if(flag && binaryString[i] == 1)
            flag = 0;
        else if(!flag && binaryString[i] == 1)
            flag = 1;
        
        if(flag)
            printf("__|\u203E\u203E");
        else
            printf("\u203E\u203E|__");
    }
    printf("\n 0v\u203E");

    for(int i=0; i< length; i++)
    {
        printf("¦    ");
    }
    printf("¦\n ");









}