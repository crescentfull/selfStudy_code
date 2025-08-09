def find_broken_segment(number_list):
    n = len(number_list)
    if n < 3:
        return []
    d0 = number_list[1] - number_list[0]
    res = []
    prev_diff = d0
    for i in range(2, n):
        diff = number_list[i] - number_list[i - 1]
        if prev_diff == d0 and diff != d0:
            res.append(i)
        prev_diff = diff
    return res


# ---------------------------
# 테스트케이스 (여러 시작 인덱스 포함)
# ---------------------------
TESTS = [
    # 예시 다중 시작
    ([1,2,3,4,5,7,9,10,11,12,16,17,18,40], [5,10,13]),

    # 다중 시작 (비등차 → 복귀 → 다시 비등차 → 복귀 → 다시 비등차)
    ([0,2,4,6,8,9,10,11,20,22,24,25,26,40,41,50], [5,11]),
    ([0,5,10,15,20,21,22,27,32,37,39,44,49,50,55,60], [5,10,13]),
    ([0,2,4,8,10,12,14,20,22,24,28], [3,7,10]),
    ([10,12,14,16,18,17,16,18,20,22,21,20,22,24,26,25,24,26,28,30], [5,10,15]),

    # 0 증가량 기반 다중 시작
    ([5,5,5,5,9,9,5,5,0,0,0,1], [4,6,8,11]),

    # 음수 등차 + 다중 시작
    ([-2,-4,-6,-8,-9,-10,-8,-10,-12,-20,-22], [4,9]),

    # 단일 시작
    ([1,3,5,7,10,100,102,104], [4]),

    # 시작 없음
    ([2,4,6,8,10,12], []),

    # 큰 수 혼합
    ([0,10**9,2*10**9,3*10**9,5*10**9,6*10**9,7*10**9,8*10**9,8*10**9+5,9*10**9,10*10**9], [4,8]),
]

if __name__ == "__main__":
    all_ok = True
    for idx, (arr, expected) in enumerate(TESTS, 1):
        got = find_broken_segment(arr)
        ok = (got == expected)
        all_ok &= ok
        print(f"#{idx:02d} got={got} expected={expected} {'OK' if ok else 'FAIL'}")
    print("\nRESULT:", "ALL PASS" if all_ok else "SOME FAILED")
