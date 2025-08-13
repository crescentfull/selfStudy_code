'''
문제
logs = [(user, score), ...]와 정수 k가 주어진다.
각 사용자별 최고 점수만 반영해 상위 k명을 반환하라.
정렬 기준은 점수 내림차순 → 사용자 이름 사전순 오름차순이다.

접근
해시맵 best[user] = max(best[user], score)로 최고점 집계

best.items()를 정렬키 (-score, user)로 정렬 후 상위 k 슬라이스
'''

def solution(logs, k):
    best = {}
    for user, score in logs:
        if user not in best or best[user]   < score:
            best[user] = score
            
    ranked = sorted(best.items(), key=lambda x: (-x[1], x[0]))
    return ranked[:k]

logs = [("a",50),("b",70),("a",90),("c",90),("c",80)]
k = 2
# 반환: [("a", 90), ("c", 90)]

print(solution(logs, k))