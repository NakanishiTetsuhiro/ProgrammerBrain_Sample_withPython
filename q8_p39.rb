N = 12

def move(log)

    return 1 if log.size == N + 1 # もし変数logの要素の数がN + 1だったら、1をreturnする

    cnt = 0

    [[0,1],[0,-1],[1,0],[-1,0]].each{|d| # 多次元配列上で前後左右に移動してみる（オブジェクトの要素が1つずつ変数dに入ってループが回っていく）

        x = log[-1][0] + d[0]
        y = log[-1][1] + d[1]

        next_pos = [x, y]

        if !log.include?(next_pos) then
            cnt += move(log + [next_pos])
            p cnt
            # sleep(0.5)
        end
    }

    cnt

end

puts move([[0,0]])
