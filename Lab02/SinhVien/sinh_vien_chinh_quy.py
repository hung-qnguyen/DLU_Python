


from sinh_vien import SinhVien


class SinhVienChinhQuy(SinhVien):
    def __init__(self, ma_so: int, ho_ten: str, ngay_sinh: str,
                 diem_rl: int) -> None:
        super().__init__(ma_so, ho_ten, ngay_sinh)
        self.diemRL = diem_rl

    def __str__(self) -> str:
        return super().__str__() + f"\t{self.diemRL}"