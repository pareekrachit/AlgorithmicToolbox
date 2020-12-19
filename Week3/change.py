# Uses python3
import sys

def get_change(m):
    ten_deno = m // 10
    m = m % 10
    five_deno = m // 5
    m = m % 5
    one_deno = m
    return (ten_deno+five_deno+one_deno)

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))