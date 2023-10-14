import sys


class PhanSo:
    def __init__(self, tu: int = 0, mau: int = 1) -> None:
        if mau == 0:
            raise ArithmeticError('Phan so khong the co mau bang 0')
        self.tu = tu
        self.mau = mau
        self.rutGon()

    
    def tinhGiaTriCuaPhanSo(self) -> float:
        return self.tu / self.mau

    def ktPhanSoAm(self):
        return self.tu * self.mau < 0

    # gcd: greatest common divisor of the two integers(UCLN)
    def findGDC(self, num1: int, num2: int):
        if num2 == 0:
            return num1
        else:
            return self.findGDC(num2, num1 % num2)

    def rutGon(self):
        gcd = self.findGDC(self.tu, self.mau)
        if gcd != 1:
            self.tu = self.tu // gcd
            self.mau = self.mau // gcd

    def __add__(self, other):
        result = PhanSo(self.tu * other.mau + self.mau * other.tu, self.mau *
                        other.mau)
        result.rutGon()
        return result
    def __sub__(self, other):
        result = PhanSo(self.tu * other.mau - self.mau * other.tu,
                        self.mau * other.mau)
        result.rutGon()
        return result

    def __mul__(self, other):
        result = PhanSo(self.tu * other.tu, self.mau * other.mau)
        result.rutGon()
        return result

    def __truediv__(self, other):
        result = PhanSo(self.tu * other.mau, self.mau * other.tu)
        result.rutGon()
        return result

    def __str__(self):
        if self.mau == 1:
            return f'{self.tu}'
        return f'{self.tu}/{self.mau}'



phanSo1 = PhanSo(-1, 2)
phanSo2 = PhanSo(5, 8)
phanSo3 = PhanSo(15, 5)
phanSo4 = PhanSo(20, 20)
print(f'{phanSo1} + {phanSo2} = {phanSo1.__add__(phanSo2)} ')
print(f'{phanSo1} - {phanSo2} = {phanSo1.__sub__(phanSo2)} ')
print(f'{phanSo1} * {phanSo2} = {phanSo1.__mul__(phanSo2)} ')
print(f'{phanSo1} : {phanSo2} = {phanSo1.__truediv__(phanSo2)} ')
phanSo1.rutGon()
phanSo2.rutGon()
phanSo3.rutGon()
phanSo4.rutGon()
