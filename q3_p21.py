uraomote_list = [0] * 100

for i in range(2, 100):
    for idx, val in enumerate(uraomote_list):

        # print(type(idx), type(val))
        # print((idx+1) % i == 0)
        
        if (idx+1) % i == 0:
            if val == 0:
                uraomote_list[idx] = 1  
            elif val == 1:
                uraomote_list[idx] = 0

# print(uraomote_list.count(0))



