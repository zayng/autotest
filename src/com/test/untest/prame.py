"""
Created on '2015/12/29'

@author: '119937'
"""


def is_prime(n):
    dat = []
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            dat.append(n % i)
        if 0 in dat:
            return False
        else:
            return True
if __name__ == "__main__":
    print(is_prime(7))
