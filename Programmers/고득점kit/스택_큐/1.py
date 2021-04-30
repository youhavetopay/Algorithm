# 다리지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    print(truck_weights)

    bridge_car = [0] * bridge_length
    lastTruckNum = truck_weights[-1]
    nowFinishTruck = 0
    count = 0
    bridge = 0
    while count < len(truck_weights) or bridge_car != [0] * bridge_length:
        nowFinishTruck = bridge_car[0]
        bridge -= bridge_car[0]
        del bridge_car[0]
        answer += 1
        if len(truck_weights) > 0:
            if bridge + truck_weights[0] <= weight:
                
                bridge_car.append(truck_weights[0])
                bridge += truck_weights[0]
                nowFinishTruck = bridge_car[0]
                
                del truck_weights[0]
                count += 1
                
                continue

        
        bridge_car.append(0)
        

    return answer

print(solution(5,5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))