'''
Created on 2017. 7. 23.

@author: duddn
'''

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('Memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('Memo.txt')
    memo = f.read()
    f.close()
    print(memo)