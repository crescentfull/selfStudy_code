#include <stdio.h>

// /* 자동변수 auto */
// void main(){
//     int i = 1;
//     auto int j = 2;
//     {/* 블록 1 */
//         int i = 3;
//         {/* 블록 2 */
//             int i = 4;
//             printf("블록 2의 i = %d\n", i);
//             printf("블록 2의 j = %d\n", j);
//         }
//         printf("블록 1의 i = %d\n", i);
//         printf("블록 1의 j = %d\n", j);
//     }
//     printf("void main() 함수내의 i = %d\n", i);
//     printf("void main() 함수내의 j = %d\n", j);
// }

void main(){
    int *p, i = 3, j;
    printf("p , i 주소 값 할당 전= %x\n", p);
    p = &i;
    printf("p , i 주소 값 할당 후 = %x\n", p);
    j = *p;
    printf("j = %d\n", j);
    j++;

    printf("*p = %d\n", *p);
    printf("p , i 주소 값 할당 후 = %x\n", p);
    printf("j++ = %d\n", j);
}