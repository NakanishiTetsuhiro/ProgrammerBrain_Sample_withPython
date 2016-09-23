num = 11

while num < 1111111:

    # [::-1] 文字列の末尾から1個ずつ遡って先頭まで要素を取り出す
    # format(num, 'o') numを8進数の文字列に変換
    # format(num, 'b') numを2進数の文字列に変換

    if str(num) == str(num)[::-1] and format(num, 'o') == format(num, 'o')[::-1] and format(num, 'b') == format(num, 'b')[::-1]:
        print(num)

    num += 2
