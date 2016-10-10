#! /usr/bin/python
# -*- coding: utf-8 -*-

# 参考URL: https://gist.github.com/shun91/30eaa2feab0852604baa

import sys


if __name__ =='__main__':
    ans = []

    sign = ['', '+', '-', '*', '/']

    for n1 in range(0, 10):
        for n2 in range(0, 10):
            for n3 in range(0, 10):
                for n4 in range(0, 10):
                    for s1 in sign:
                        for s2 in sign:
                            for s3 in sign:
                                calc_strings = str(n1) + s1 + str(n2) + s2 + str(n3) + s3 + str(n4)
                                num_reverse = str(n4) + str(n3) + str(n2) + str(n1)

                                print(calc_strings)
                                
                                try:
                                    if s1 == '' and s2 == '' and s3 == '':
                                        continue
                                    if str(eval(calc_strings)) == num_reverse:
                                        ans.append(calc_strings)
                                except:
                                    pass
    print(ans)
