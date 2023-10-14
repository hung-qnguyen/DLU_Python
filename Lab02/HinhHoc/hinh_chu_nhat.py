from hinh_hoc import HinhHoc


class HinhChuNhat(HinhHoc):
    def __init__(self, rong: float, dai: float) -> None:
        super(HinhChuNhat, self).__init__(rong)
        self._dai = dai

    @property
    def chieuDai(self) -> float:
        return self._dai

    @property
    def chieuRong(self) -> float:
        return self._canh

    def __str__(self) -> str:
        return f"Hinh chu nhat co chieu rong: {self._canh} va chieu dai:" \
               f" {self._dai}"

    def xuat(self) -> None:
        print(f"Hinh chu nhat co chieu rong: {self._canh} va c"
              f"hieu dai: {self._dai}")

    def tinhDienTich(self) -> float:
        return self._dai * self._canh
