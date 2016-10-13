def cutbar(m, n, current):
    if current >= n:    # 切り終えたら０を返す
        return 0

    elif current < m:
        return 1 + cutbar(m, n, current * 2)    # 関数の再帰呼出し。人の数が現在の個数を超える場合、次回は必ず現在の２倍の個数になる

    else:
        return 1 + cutbar(m, n, current + m)    # 人の数が現在の個数を超えない場合、次回は人の数分個数が増える
  

print (cutbar(3, 20, 1))
print (cutbar(5, 100, 1))
