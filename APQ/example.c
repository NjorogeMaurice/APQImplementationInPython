#include <stdio.h>

int main(){
    int x, s;
    s = 0;
    printf("Maurice Njoroge SCT211-0005/2020\n");
    while(1){
        printf("#?");
        scanf("%d", &x);
        if(x == 0)
            break;
        s = s + x;
        printf("Sum = %d\n",s);
        
    }

    return 0;
}