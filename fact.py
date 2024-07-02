
my_number = 456

#재귀: 함수 내부에서 자기 자신을 호출
def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1) * n


def my_max(x, y):
    if x > y:
        return x
    else:
        return y