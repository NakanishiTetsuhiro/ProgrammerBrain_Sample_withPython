N = 12


def move(log):

    if len(log) == N + 1:                   # もし変数logの要素の数がN + 1だったら、1をreturnする
        return 1

    cnt = 0

    for i in [[0,1],[0,-1],[1,0],[-1,0]]:   # 多次元配列上で前後左右に移動してみる

        x = log[-1][0] + i[0]
        y = log[-1][1] + i[1]

        next_pos = [x, y]

        if next_pos not in log:             # next_posがlogに含まれているか確認
            cnt += move(log + [next_pos])

    return cnt


print(move( [[0,0]] ))
