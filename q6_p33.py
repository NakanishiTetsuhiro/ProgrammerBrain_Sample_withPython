initial_value = 2
upper_limit   = 10000
result        = 0


while initial_value <= upper_limit:

    if initial_value % 2 == 0:
        current_num = initial_value * 3 + 1
    else:
        current_num = initial_value

    while current_num != 1 and current_num != initial_value:

        if current_num % 2 == 0:
            current_num = current_num / 2
        elif current_num % 2 == 1:
            current_num = current_num * 3 + 1
        
    if current_num == initial_value:
        result  += 1

    initial_value += 2
    
        
print("result : " + str(result))
