from sinh_vien import SinhVien


class DanhSachSv:
    def __init__(self):
        self.dssv = []

    def themSinhVien(self, *sinh_vien: SinhVien):
        self.dssv.append(sinh_vien)

    def docFile(self, ten_file):
        f = open(ten_file)
        dong = f.readlines()
        for i in dong:
            self.dssv.append(SinhVien(i))

    def xuat(self):
        for sinh_vien in self.dssv:
            print(sinh_vien)

    def timSVTheoMS(self, ma_so):
        return [sinh_vien for sinh_vien in self.dssv if sinh_vien.maSo == ma_so]

    def timVTSVTheoMS(self, ma_so: int) -> int:
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ma_so:
                return i
        return -1

    def xoaSVTheoMS(self, ma_so: int) -> bool:
        vt = self.timVTSVTheoMS(ma_so)
        if vt != -1:
            del self.dssv[vt]
            return True
        return False

    def timSVTheoTen(self, ten_tk: str):
        return [sinh_vien for sinh_vien in self.dssv if
                sinh_vien.hoTen.lower().__contains__(ten_tk.lower())
                ]

    def timSVSinhTruocNgay(self, ngay_sinh: str):
        return [sinh_vien for sinh_vien in self.dssv if sinh_vien.ngaySinh <
                sinh_vien.dateParse(ngay_sinh)]

    def sapXepSVTheoHoTen(self):
        self.dssv.sort(key=lambda x: x.hoTen)


#
# sv1 = SinhVien(2011123, 'Nguyen Van A',
#                "01/01/2000")
# sv2 = SinhVien(2011125, 'Nguyen Van B',
#                "05/12/2000")
# sv3 = SinhVien(2011128, 'Nguyen Van C',
#                "18/11/1998")
# sv4 = SinhVien(2022402, 'Nguyen Van D',
#                "02/02/2001")

# dsSinhVien = DSSinhVien()
# dsSinhVien.themSinhVien(sv1)
# dsSinhVien.themSinhVien(sv2)
# dsSinhVien.themSinhVien(sv3)
# dsSinhVien.themSinhVien(sv4)
#
# dsSinhVien.xuat()
# dsSinhVien.xoaSVTheoMS(2011123)
# print('Danh sach sinh vien da xoa: ')
# dsSinhVien.xuat()

# name = 'Nguyen Van D'
# print(f'Sinh vien co ten {name} la: ')
# result = dsSinhVien.timSVTheoTen(name)
# for sv in result:
#     print(sv)
#

# print('Danh sach sinh vien la: ')
# dsSinhVien.docFile('sv.txt')
# dsSinhVien.xuat()

# ngayTK = '01/01/2003'
# print(f'Sinh vien sinh truoc ngay {ngayTK} la: ')
# kqTimNgay = dsSinhVien.timSVSinhTruocNgay(ngayTK)
# for sv in kqTimNgay:
#     print(sv)
# print('Danh sach sau khi sap xep: ')
# dsSinhVien.sapXepSVTheoHoTen()
# dsSinhVien.xuat()