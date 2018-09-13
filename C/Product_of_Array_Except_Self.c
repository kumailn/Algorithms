#include <stdio.h>

main(){
    int age = 3;
    printf("I am %d years old!", &productExceptSelf([1, 2, 8], 3, 3)[0]);
}

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int result[numsSize];
    int i = 0;
    for(i; i < numsSize; i++){
       result[i] = 2; 
    }  
    result[0] = 5;
    int* iii = result[0];
    return iii;
}
