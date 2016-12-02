from datetime import date, timedelta


def daterange(start_date, end_date):

    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)


if __name__ == '__main__':

    start = date(1964, 10, 10)
    end = date(2020, 7, 24)
    results = []
    
    for i in daterange(start, end):
        tmp_date = int(i.strftime("%Y%m%d")) # ８桁のフォーマットに合わせる
        tmp_date_binnum_reverse = format(tmp_date, 'b')[::-1]
        tmp_date_binnum_reverse_decimalnum = int(tmp_date_binnum_reverse, 2)
        if tmp_date == tmp_date_binnum_reverse_decimalnum:
            results.append(tmp_date)

    print(results)
        
