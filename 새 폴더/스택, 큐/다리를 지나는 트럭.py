def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    bridge_weight = 0
    
    while True:
        if len(truck_weights) == 0 and sum(bridge) == 0:
            break
            
        answer += 1
        if bridge != 0:
            bridge_weight -= bridge[0]
        del bridge[0]
        
        if truck_weights:
            if len(bridge) <= bridge_length and bridge_weight + truck_weights[0] < weight:
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights[0])
                del truck_weights[0]
            
    return answer
solution(2, 10, [7,4,5,6])