#include <stdio.h>  // 표준 입출력 함수들을 사용하기 위해 stdio.h 헤더 파일을 포함

    /*
    자료형들은 시스템, 컴파일러, 운영체제에 따라 크기가 달라진다.
    특히 정수형 자료형인 long은 대부분 4비트이지만, 64비트와 리눅스, mac OS 운영체제에서는 8비트를 가진다.
    */

/* 메인 함수 */
void main() {// 메인 함수 시작
    /* char 자료형 */
    printf("char 자료형 크기 : %d byte\n", sizeof(char)); // sizeof() 자료형 및 객체의 크기를 바이트 단위로 반환해주는 함수
            // char 자료형의 크기를 출력, char는 문자 데이터를 저장하는 데 사용, 1바이트
    printf("signed char 자료형 크기 : %d byte\n", sizeof(signed char));
            // signed char 자료형의 크기를 출력, signed char는 부호 있는 문자 데이터를 저장하는 데 사용, 1바이트
    printf("unsigned char 자료형 크기 : %d byte\n", sizeof(unsigned char));
            // unsigned char 자료형의 크기를 출력, unsigned char는 부호 없는 문자 데이터를 저장하는 데 사용, 1바이트

    /* 정수형 자료형 */
    // short, int, long, long long 자료형

    // int의 크기를 나타내는 short, long 키워드를 붙여 정의할 수 있다.
    // 부호 있는 정수를 나타내는 signed 키워드, 부호 없는 정수를 나타내는 unsigned 키워드가 있다.
    // 보통 부호 있는 정수를 나타낼때 signed 키워드는 생략, 또한 다른 키워드와 사용할 때는 int를 생략가능
    // ! int, unsigned int와 같이 자료형이 같다면 부호 여부와 관계없이 크기가 같지만 부호가 있는 정수는 음수를 나타내야 하므로 
    // ! 양수를 나타내는 표현 범위가 부호 없는 정수보다 1/2로 줄어든다.

    /* short */   
    printf("short 자료형 크기 : %d byte\n", sizeof(short)); 
            // short 자료형은 정수, 2바이트
    printf("short int 자료형 크기 : %d byte\n", sizeof(short int));
            // short int 자료형은 short와 같다, 2바이트
    printf("signed short 자료형 크기 : %d byte\n", sizeof(signed short));
    printf("signed short int 자료형 크기 : %d byte\n", sizeof(signed short int));
            // signed short와 signed short int 자료형은 부호 있는 short 자료형과 같다, 2바이트
    printf("unsigned short 자료형 크기 : %d byte\n", sizeof(unsigned short));
    printf("unsigned short int 자료형 크기 : %d byte\n", sizeof(unsigned short int));
            // unsigned short와 unsigned short int 자료형은 부호 없는 정수를 저장, 2바이트
    /* int */
    printf("int 자료형 크기 : %d byte\n", sizeof(int));
            // int 자료형, 4바이트
    printf("signed int 자료형 크기 : %d byte\n", sizeof(signed int));
            // signed int 자료형은 부호 있는 int와 같다, 4바이트
    printf("unsigned 자료형 크기 : %d byte\n", sizeof(unsigned));
            // unsigned 자료형은 부호 없는 정수를 저장, 4바이트
    printf("unsigned int 자료형 크기 : %d byte\n", sizeof(unsigned int));
            // unsigned int 자료형은 부호 없는 int와 같다, 4바이트
    /* long */
    printf("long 자료형 크기 : %d byte\n", sizeof(long));
            // long 자료형은 4바이트 또는 8바이트
    printf("long int 자료형 크기 : %d byte\n", sizeof(long int));
            // long int 자료형은 long과 같다, 4바이트 또는 8바이트
    printf("signed long 자료형 크기 : %d byte\n", sizeof(signed long));
    printf("signed long int 자료형 크기 : %d byte\n", sizeof(signed long int));
            // signed long와 signed long int 자료형은 부호 있는 long 자료형과 동일, 4 또는 8바이트
    printf("unsigned long 자료형 크기 : %d byte\n", sizeof(unsigned long));
    printf("unsigned long int 자료형 크기 : %d byte\n", sizeof(unsigned long int));
            // unsigned long와 unsigned long int 자료형은 부호 없는 정수를 저장, 4 또는 8바이트
    /* long long */
    printf("long long 자료형 크기 : %d byte\n", sizeof(long long));
            // long long 자료형, 8바이트
    printf("long long int 자료형 크기 : %d byte\n", sizeof(long long int));
            // long long int 자료형은 long long과 같다, 8바이트
    printf("signed long long 자료형 크기 : %d byte\n", sizeof(signed long long));
    printf("signed long long int 자료형 크기 : %d byte\n", sizeof(signed long long int));
            // signed long long와 signed long long int 자료형은 부호 있는 long long 자료형과 같다, 8바이트
    printf("unsigned long long 자료형 크기 : %d byte\n", sizeof(unsigned long long));
    printf("unsigned long long int 자료형 크기 : %d byte\n", sizeof(unsigned long long int));
            // unsigned long long와 unsigned long long int 자료형은 부호 없는 정수를 저장, 8바이트

    /* 실수형 자료형*/
    // float, double, long double 자료형은 실수 데이터를 저장
    // 실수 자료형은 실수와 소수점을 2진수로 표현하는 부동 소수점 표현 방법을 사용
    // 부동소수점 저장에 관한 규약은 IEEE 754로 0과 1로 저장되는 내용의 일정 부분을 비트단위로 나누어 부호, 가수, 지수를 저장하여 실수를 표현한다.
    printf("float 자료형 크기 : %d byte\n", sizeof(float));
            // float 자료형, 4바이트
            //단정밀도(single-precision) 부동소수점
    printf("double 자료형 크기 : %d byte\n", sizeof(double));
            // double 자료형, 8바이트
            // 배정밀도(double-precision) 부동소수점
    printf("long double 자료형 크기 : %d byte\n", sizeof(long double));
            // long double 자료형은 확장된 정밀도의 부동소수점 값을 저장, 시스템에 따라 크기가 다를 수 있다.
            // 일반적으로 8바이트 또는 16바이트 크기
} // 함수 끝