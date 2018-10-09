// comment

#include <stdio.h>
#include <string.h>

#define MYNAME "Kumail"

int num = 12;

main(){
    int age = 4;
    // printf("print this\n\n");
    // printf("I am %d years old!", age);

    // if(age == 6){
    //     printf("NEW AGE1: %d", age);
    // }
    // else if(age = 7){
    //     printf("NEW AGE2: %d", age);
    // }
    float ff = 2.12345678;
    int d = 4;
    printf("Floaty: %d\n", ff);
    switch(age){
        case 1:
            printf("one");
            break;
        case 3 ... 5:
            printf("3 to 5");
            break;
        default:
            printf("REFWE");

    };
}