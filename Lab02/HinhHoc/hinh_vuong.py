

from hinh_chu_nhat import HinhChuNhat


class HinhVuong(HinhChuNhat):
    def __init__(self, cd: float):
        super(HinhVuong, self).__init__(cd, cd)

    @property
    def canhHV(self) -> float:
        return self._dai

    def __str__(self) -> str:
        return f"Hinh vuong co do dai canh la: {self._dai}"

    def xuat(self) -> None:
        print(f"Hinh vuong co do dai canh la: {self._dai}")

    def tinhDienTich(self) -> float:
        return self._dai ** 2
