# 세 정수의 최대값 구하기

def max3(a, b, c):
    """a, b, c의 최댓값을 구하여 반환"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum 

    return maximum
    
print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')