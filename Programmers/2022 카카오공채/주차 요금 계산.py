from collections import defaultdict
import math

def convertTimeToMinute(time):

    h, m = map(int, time.split(':'))

    m += h * 60

    return m

def getTotalParkingTime(times):

    total_time = 0
    for i in range(1, len(times), 2):
        total_time += times[i] - times[i-1]
    
    return total_time

def getTotalParkingPay(total_time, fees):
    basic_time, basic_pay, minute_time, minute_pay = fees

    if total_time <= basic_time:
        return basic_pay

    
    over_time = total_time - basic_time
    return basic_pay + (math.ceil(over_time / minute_time) * minute_pay)


def solution(fees, records):

    '''
        나의 풀이
        주차 요금을 계산하는 문제

        나의 접근법
        깡 구현 문제라서 그냥 그대로 구현함
        시간은 분단위로 전부 바꿔서 계산을 했고
        출차시간이 없다면 23:59분을 넣어주는 방식으로 
        계산하는 방식으로 함

        이런 뭔가 실제 도메인을 구현하는 구현 문제는
        좀 재밌는거 같음 ㅋㅋㅋ
    '''

    answer = []

    in_out_table = defaultdict(list)

    for record in records:
        time, car_num, in_out = record.split(' ')

        m = convertTimeToMinute(time)
        in_out_table[car_num].append(m)
    
    for key in in_out_table:
        if len(in_out_table[key]) % 2 != 0:
            in_out_table[key].append(convertTimeToMinute('23:59'))


    pays = []
    for car_num, times in in_out_table.items():
        total_parking_time = getTotalParkingTime(times)
        total_parking_pay = getTotalParkingPay(total_parking_time, fees)
        pays.append([car_num, total_parking_pay])

    pays.sort(key=lambda x: x[0])

    for car_num, pay in pays:
        answer.append(pay)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

class Parking:
    def __init__(self, fees) -> None:
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout == 'IN' else False
        if self.in_flag: self.in_time = str2int(t)
        else:            self.total  += (str2int(t)-self.in_time)
    
    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + math.ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def firstSolu(fees, records):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/92341/solution_groups?language=python3

        클래스를 통해 아주 깔끔하게 풀어낸듯 함 ㅋㅋ
        가로 정렬까지 한게 좀 인상적임 ㅋㅋㅋㅋ

    '''

    recordsDict = defaultdict(lambda: Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]