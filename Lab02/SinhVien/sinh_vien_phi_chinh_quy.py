

from sinh_vien import SinhVien


class SinhVienPhiChinhQuy(SinhVien):
    def __init__(self, ma_so: int, ho_ten: str, ngay_sinh: str,
                 trinh_do: str, tgdt: float):
        super().__init__(ma_so, ho_ten, ngay_sinh)
        self.thoiGianDaoTao = tgdt
        self.trinhDo = trinh_do

    def __str__(self) -> str:
        return super().__str__() + f'\t{self.trinhDo}\t{self.thoiGianDaoTao}'