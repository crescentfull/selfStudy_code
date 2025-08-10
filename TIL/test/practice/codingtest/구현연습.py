'''
1번 에디터 시뮬레이터 (스택 2개)
포인트: 커서 이동·삽입·삭제를 O(1)로 시뮬레이션
입력: 첫 줄 초기 문자열 S, 둘째 줄 명령 개수 M, 이후 M줄에 L|D|B|P x
출력: 최종 문자열

예시입력:
abcd
7
P x
L
L
B
P y
D
P z

예시 출력:
abydzx
'''
import sys
from typing import List

def solution(s, commands):
    left_stack =  list(s)
    right_stack = []
    
    
    for command in commands:
        if command[0] == 'L' and left_stack:
            right_stack.append(left_stack.pop())
        elif command[0] == 'D' and right_stack:
            left_stack.append(right_stack.pop())
        elif command[0] == 'B' and left_stack:
            left_stack.pop()
        elif command[0] == 'P':
            left_stack.append(command[1])

    left_stack.extend(reversed(right_stack))
    return ''.join(left_stack)


# 너의 solution 시그니처/동작에 맞춘 테스트 하네스
def run_tests():
    tests = [
        # 1) 기본 예시 (수정된 정답)
        ("T1_example_fixed",
         "abcd",
         [("P","x"), "L", "L", "B", ("P","y"), "D", ("P","z")],
         "abydzx"),

        # 2) 빈 문자열 시작 + 경계 이동
        ("T2_empty_and_moves",
         "",
         ["B", "L", "D", ("P","A"), ("P","B"), "L", ("P","C")],
         "ACB"),

        # 3) 연속 삭제 후 삽입
        ("T3_mass_delete_then_insert",
         "aaaa",
         ["B","B","B","B","B", ("P","x"), ("P","y")],
         "xy"),

        # 4) 좌우 왕복 이동 후 삽입
        ("T4_back_and_forth",
         "xyz",
         ["L","L", ("P","A"), "D", ("P","B"), "D", ("P","C")],
         "xAyBzC"),

        # 5) 맨 앞으로 이동해 삽입 후 다시 끝으로
        ("T5_front_inserts_then_end",
         "hello",
         ["L"]*5 + [("P","_")]*3 + ["D"]*5,
         "___hello"),

        # 6) 오른쪽 스택이 2개 이상일 때 '뒤집어' 붙는지 확인
        ("T6_right_stack_reversal",
         "abc",
         ["L","L", ("P","X"), ("P","Y")],
         "aXYbc"),

        # 7) 오른쪽 비어있을 때 D는 무시되는지
        ("T7_right_empty_D_ignored",
         "ab",
         ["D","D","D"],   # 이미 커서가 끝(오른쪽 비어있음)
         "ab"),

        # 8) 왼쪽 비어있을 때 L/B 무시
        ("T8_left_empty_LB_ignored",
         "",
         ["L","B", ("P","K")],
         "K"),

        # 9) 숫자/특수문자 삽입도 동작
        ("T9_non_alpha_chars",
         "AA",
         ["L", ("P","1"), ("P","-"), "D", ("P","!")],
         "A1-A!"),  # 주의: 공백도 정상 처리됨
    ]

    all_ok = True
    for name, s, cmds, expected in tests:
        got = solution(s, cmds)
        print(f"{name:>20}: expected={expected!r} | got={got!r}")
        if got != expected:
            all_ok = False
    assert all_ok, "❌ 일부 테스트가 실패했습니다."
    print("\n✅ 모든 테스트 통과!")

# 실행
run_tests()
