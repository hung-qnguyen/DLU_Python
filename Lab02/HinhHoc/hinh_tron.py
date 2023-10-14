import math

from hinh_hoc import HinhHoc



class HinhTron(HinhHoc):
    def __init__(self, ban_kinh: float) -> None:
        super(HinhTron, self).__init__(ban_kinh)

    @property
    def banKinh(self) -> float:
        return self._canh

    def __str__(self) -> str:
        return f"Hinh tron co ban kinh la {self._canh}"

    def xuat(self) -> None:
        print(f"Hinh tron co ban kinh la {self._canh}")

    def tinhDienTich(self) -> float:
        return math.pi * self._canh ** 2
