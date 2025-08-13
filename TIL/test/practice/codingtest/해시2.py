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

