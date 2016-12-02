# Q. 以下の手順を踏んだ時、元の日付と同じになる日にちを答えよ。期間は1964/10/10から2020/07/24
#
# 1. 日付のフォーマットはYYYYMMDD
# 2. 2進数に変換
# 3. 2進数を逆から並べる
# 4. 逆から並べた2進数を10進数に戻す


from datetime import date, timedelta


# dateオブジェクトを投げるとrangeしてくれるすごいやつ
def daterange(start_date, end_date):

    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)


if __name__ == '__main__':

    start   = date(1964, 10, 10)
    end     = date(2020, 7, 24)
    results = []
    
    for i in daterange(start, end):
        tmp_date = int(i.strftime("%Y%m%d")) # ８桁のフォーマットに合わせる
        tmp_date_binnum_reverse = format(tmp_date, 'b')[::-1] # 2進数にしてReverse
        tmp_date_binnum_reverse_decimalnum = int(tmp_date_binnum_reverse, 2) # 10進数に変換

        if tmp_date == tmp_date_binnum_reverse_decimalnum:
            results.append(tmp_date)

    print(results)
        
