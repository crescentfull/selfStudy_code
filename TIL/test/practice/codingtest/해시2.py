'''
문제
요금 정책 fees = [base_time, base_fee, unit_time, unit_fee]와
입·출차 기록 records = ["HH:MM CAR IN/OUT", ...]가 주어진다.
출차 기록이 없는 차량은 23:59에 출차한 것으로 간주한다.
차량 번호 오름차순으로 각 차량의 총 요금을 리스트로 반환하라.

접근
해시맵으로 진입 중인 차량의 시각 기록: in_time[car] = minutes

OUT이 나오면 누적 시간 total[car] += now - in_time[car] 갱신 후 in_time에서 제거

모든 기록 처리 후 in_time에 남은 차량은 23:59로 정산

총 주차 시간으로 요금 계산:

기본시간 이하면 base_fee

초과분은 ceil((t - base_time)/unit_time) * unit_fee 추가

차량 번호 오름차순으로 요금 나열
'''

import math

def parse_time(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def calc_fee(total_min, fees):
    base_t, base_f, unit_t, unit_f = fees
    if total_min <= base_t:
        return base_f
    extra = total_min - base_t
    units = math.ceil(extra/unit_t)
    return base_f + units * unit_f

def parking_fees(fees, records):
    in_time = {}
    total = {}
    for rec in records:
        t, car, typ = rec.split()
        minutes = parse_time(t)
        
        if typ == 'IN':
            in_time[car] = minutes
        else:
            start = in_time.pop(car)
            total[car] = total.get(car, 0) + (minutes - start)

    # 남아있는 차량은 23:59에 출차 처리
    end_of_day = parse_time("23:59")
    for car, start in in_time.items():
        total[car] = total.get(car, 0) + (end_of_day - start)

    # 차량 번호 오름차순으로 요금 계산
    result = []
    for car in sorted(total.keys()):
        result.append(calc_fee(total[car], fees))
    return result


fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
    "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
    "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"
]
# 반환: [14600, 34400, 5000]  # 차량번호 0000, 0148, 5961 순
print(parking_fees(fees, records))

# ✅ 핵심은 입차 시각만 기억했다가 출차 시 누적, 그리고 미출차는 23:59 처리 후 차량번호로 정렬하는 것이다.