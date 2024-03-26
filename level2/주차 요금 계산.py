import math
from collections import OrderedDict

def solution(fees, records):
    fee = []
    parking_lot = {}
    car = []
    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    for record in records:
        car.append(record.split(' ')[1])
    kind_car = list(set(car))
    for kind in kind_car:
        parking_lot[kind] = []

    records.sort(key=lambda x: x.split(' ')[1])
    for record in records:
        t, car_number, state = record.split(' ')
        parking_lot[car_number].append(t)
    for parking in parking_lot:
        if len(parking_lot[parking]) % 2 == 1:
            parking_lot[parking].append('23:59')
    parking_lot = OrderedDict(sorted(parking_lot.items()))
    for parking in parking_lot:
        Time = 0
        for i in range(0, len(parking_lot[parking]), 2):
            out_hour, out_minute = map(int, parking_lot[parking][i + 1].split(':'))
            in_hour, in_minute = map(int, parking_lot[parking][i].split(':'))
            if out_minute < in_minute:
                out_minute += 60
                out_hour -= 1
            Time += (out_hour - in_hour) * 60 + out_minute - in_minute
        if Time <= basic_time:
            fee.append(basic_fee)
        else:
            fee.append(basic_fee + math.ceil((Time - basic_time) / unit_time) * unit_fee)
    return fee

