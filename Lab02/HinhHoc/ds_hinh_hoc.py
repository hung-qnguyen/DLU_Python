from hinh_hoc import HinhHoc
from hinh_tron import HinhTron


class DanhSachHinhHoc:
    def __init__(self, ds=None) -> None:
        if ds is not None:
            self.dshh = list(ds)
        else:
            self.dshh = []

    def themHinhHoc(self, *args: HinhHoc) -> None:
        for i in args:
            self.dshh.append(i)

    def xuat(self) -> None:
        for hh in self.dshh:
            print(hh)

    def timHinhCoDienTichLonNhat(self) -> HinhHoc:
        return max(self.dshh, key=lambda hh: hh.tinhDienTich())

    def timHinhCoDienTichNhoNhat(self) -> HinhHoc:
        return min(self.dshh, key=lambda hh: hh.tinhDienTich())

    def timHinhTronNhoNhat(self) -> HinhHoc:
        return min([hh for hh in self.dshh if isinstance(hh, HinhTron)],
                   key=lambda hh:
                   hh.tinhDienTich())

    def sapXepGiamTheoDienTich(self) -> None:
        self.dshh.sort(key=lambda hh: hh.tinhDienTich(), reverse=True)

    def tinhTongDienTich(self) -> float:
        result = 0
        for hh in self.dshh:
            result += hh.tinhDienTich()
        return result

    def demSoLuongHinhTheoLoaiHinh(self, loai_hinh) -> int:
        return sum([1 for hh in self.dshh if isinstance(hh, loai_hinh)])

    def timHinhCoDienTichLonNhatTheoLoaiHinh(self, loai_hinh) -> HinhHoc:
        return max(
            [hh for hh in self.dshh if isinstance(hh, loai_hinh)],
            key=lambda hhh: hhh.tinhDienTich())

    def timVTDauTienCuaHinh(self, h: HinhHoc) -> int:
        for i in range(len(self.dshh)):
            if type(self.dshh[i]) == type(
                    h) and self.dshh[i].tinhDienTich() == h.tinhDienTich():
                return i
        return -1

    def xoaHinhTaiViTri(self, vt: int) -> bool:
        if len(self.dshh) > vt:
            del self.dshh[vt]
            return True
        return False

    def timHinhTheoDienTich(self, dt: float):
        return DanhSachHinhHoc(
            [hh for hh in self.dshh if hh.tinhDienTich() == dt])

    def xoaHinh(self, h: HinhHoc) -> bool:
        vt = self.timVTDauTienCuaHinh(h)
        if vt:
            del self.dshh[vt]
            return True
        return False

    def xoaHinhTheoLoai(self, loai_hinh):
        n = 0
        for i in range(len(self.dshh)):
            if isinstance(self.dshh[i - n], loai_hinh):
                del self.dshh[i - n]
                n += 1

    def xuatHinhTheoChieuTangGiam(self, kieu, giam=False) -> None:
        ds_hinh_theo_kieu = [hh for hh in self.dshh if isinstance(hh, kieu)]
        ds_hinh_theo_kieu.sort(key=lambda hh: hh.tinhDienTich(), reverse=giam)
        for hh in ds_hinh_theo_kieu:
            print(hh)

    def tinhTongDTTheoKieuHinh(self, kieu) -> float:
        result = 0
        for hh in self.dshh:
            if isinstance(hh, kieu):
                result += hh.tinhDienTich()
        return result
