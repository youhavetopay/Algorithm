def truckTour(petrolpumps):
    # Write your code here
    pumps_count = len(petrolpumps)
    check_points = [False] * pumps_count

    my_fuel = 0
    my_idx = 0
    start_idx = -1

    move_indexs = []
    while len(move_indexs) != pumps_count:

        if len(move_indexs) == pumps_count-1:
            break

        if my_fuel + petrolpumps[my_idx][0] >= petrolpumps[my_idx][1]:
            if start_idx == -1:
                start_idx = my_idx
            move_indexs.append(my_idx)
            check_points[my_idx] = True

            my_fuel += petrolpumps[my_idx][0] - petrolpumps[my_idx][1]
            
        else:
            if start_idx != -1:
                start_idx = -1
            
            check_points = [False] * pumps_count
            if move_indexs != []:
                my_idx = move_indexs[0] + 1
                move_indexs = []
        
        my_idx += 1
        if pumps_count <= my_idx:
            if move_indexs == []:
                return -1
            my_idx = 0

    # print(my_idx, check_points, start_idx)
    return start_idx

p1 = [[5, 5], [3, 3], [0, 4]]
print(truckTour(p1))