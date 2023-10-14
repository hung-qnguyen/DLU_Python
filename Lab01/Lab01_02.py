from math import pi
from math import sqrt
import math


#1. Tinh a+b, a/b, a^b
def sumOf(a, b):
    return a + b


def quotient(a, b):
    return a / b


def powerOf(a, b):
    return a ** b


print(sumOf(8, 15))
print(quotient(200, 6))
print(powerOf(2, 10))

#2 Tính diện tích hình tròn khi biết bán kính
def circleArea(r):
    return pi * r ** 2
print(circleArea(5))

#  3 Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
def isPrime(n):
    if n < 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def exportPrimes(start, end):
    print(f'The prime numbers within the sequence {start} to {end} is: ')
    for i in range(start, end):
        if isPrime(i) == 1:
            print("{0} ".format(i))

exportPrimes(0, 20)


#  4 Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
def isFibonacci(n):
    a = 0
    b = 1
    while a <= n:
        if n == a:
            return True
        a, b = b, a + b
    return False

print(
    isFibonacci(13),
    isFibonacci(2),
    isFibonacci(34)
)

#5 Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
def indexOfFibo(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return indexOfFibo(n - 1) + indexOfFibo(n - 2)

print(
    indexOfFibo(0),
    indexOfFibo(1),
    indexOfFibo(2),
    indexOfFibo(3),
    indexOfFibo(4),
    indexOfFibo(5),
    indexOfFibo(6),
    indexOfFibo(7),
    indexOfFibo(8),
    indexOfFibo(9),
    indexOfFibo(10),
    indexOfFibo(11)
)

#  6  Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)
def fibonacciSum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return indexOfFibo(n) + fibonacciSum(n - 1)


print(
    fibonacciSum(0),
    fibonacciSum(1),
    fibonacciSum(2),
    fibonacciSum(3),
    fibonacciSum(4),
    fibonacciSum(5),
    fibonacciSum(6),
    fibonacciSum(7),
    fibonacciSum(8),
    fibonacciSum(9),
    fibonacciSum(10),
    fibonacciSum(11),
)

#  7. Tính tổng căn bậc 2 của n số nguyên đầu tiên
def sumOfSqrt(n):
    if n == 0:
        return 0
    return sqrt(n) + sumOfSqrt(n - 1)

print(sumOfSqrt(10))


#  8. Giải phương trình bậc 2: ax2 + bx + c=0
def solveQuadratic(a, b, c):
    delta = (b**2) - 4 * (a * c)
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phuong trinh co 2 nghiem phan biet: {root1} va {root2}")
    elif delta == 0:
        root = -b / (2 * a)
        print(f"Phuong trinh co duy nhat 1 nghiem: {root}")
    else:
        print("Vo Nghiem")


solveQuadratic(1, -3, 2)


# #  9.  Tính n!
def factorialOf(n):
    if n == 0:
        return 1
    return n * factorialOf(n - 1)


print(factorialOf(5))


# #  10. In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
def printTriangle(n):
    for i in range(0, n):
        print("* ", end="")
        for j in range(1, i + 1):
            if j == i:
                print("* ", end="")
            elif i == n - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print("\r")


printTriangle(8)


#  11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành
# #  giờ, phút, giây. Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ:
# #  soGiay = 3770 thì xuất ra màn hình 1:2:50
#
def convertTime(seconds: int):
    hour = seconds // 360
    diff = seconds - gio * 360
    min = diff // 60
    sec = diff - min * 60
    print(f"{hour}:{min}:{sec}")


convertTime(3770)


#  12. Cho một mảng số nguyên: (nên viết 2-3 cách)


#  a) Xuât tất cả các số lẻ không chia hết cho 5
def printOdd5(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0 and number % 5 != 0:
            print(
                "Odd numbers not divisible by 5 between {} and {}:".format(start, end)
            )

printOdd5(1, 20)


#  b) Xuất tất cả các số Fibonacci
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 19, 23]
list2 = [4, 6, 9, 6, 3, 4, 7, 8, 9, 16, 19, 17, 13]


def printFibonacci(list1):
    print("Cac so Fibonaci la: ")
    for i in range(len(list1)):
        if isFibonacci(list1[i]):
            print(list1[i], end=" ")
    print("\r")
    
printFibonacci(list1)
printFibonacci(list2)
