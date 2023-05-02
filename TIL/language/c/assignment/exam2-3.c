#include "exam2-3.h"
        // 사용자 정의 헤더 파일인 "exam2-3.h"를 선정처리기인 #include 를 선언해서 포함 시킨다.
        // exam2-3.h 파일에 이미 stdio.h가 포함되어 있으므로, 여기서는 stdio.h를 다시 포함시킬 필요가 없다.

/* 메인 함수 */
void main(){ // 함수 시작
    int add_result, sub_result; // 정수형 변수 add_result와 sub_result를 선언
        // 각각 덧셈 결과와 뺄셈 결과를 저장

    printf("10과 5를 더하면 %d이다. \n", ADD(10,5)); // ADD 매크로를 사용하여 10과 5를 더한 결과를 출력
        // ADD 매크로는 "exam2-3.h" 사용자 헤더 파일에 정의
        // 결과는 정수형이므로 %d로 표시되며, 두 수를 더한 결과가 출력

    printf("10에서 5를 빼면 %d이다. \n", SUB(10,5)); // SUB 매크로를 사용하여 10에서 5를 뺀 결과를 출력
        // SUB 매크로는 "exam2-3.h" 사용자 헤더 파일에 정의
        // 결과는 정수형이므로 %d로 표시되며, 두 수를 뺀 결과가 출력됩니다.
} // 함수 끝