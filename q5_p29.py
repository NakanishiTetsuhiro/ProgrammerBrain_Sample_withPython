# 硬貨は最大で15枚まで

count = 0

for gohyakuen in range(2):
    for hyakuen in range(15):
        for gojuen in range(15):
            for juen in range(15):
                maisu = gohyakuen + hyakuen + gojuen + juen
                kingaku = gohyakuen*500 + hyakuen*100 + gojuen*50 + juen*10

                if maisu <= 15 and kingaku == 1000:
                    count += 1

print(count)


