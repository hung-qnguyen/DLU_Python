from ds_hinh_hoc import DanhSachHinhHoc
from hinh_chu_nhat import HinhChuNhat
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong
from loai_hinh import LoaiHinh


hinhTron1 = HinhTron(4)
hinhTron2 = HinhTron(3)
hinhTron3 = HinhTron(1.5)
print(f"Ban kinh la: {hinhTron1.banKinh}")

print(f"Dien tich hinh tron 1 la {hinhTron1.tinhDienTich()}")

hinhChuNhat1 = HinhChuNhat(5, 2)
hinhChuNhat2 = HinhChuNhat(6, 3)
hinhChuNhat3 = HinhChuNhat(10, 7)
print(f'Chieu dai la: {hinhChuNhat1.chieuDai}')
print(f'Chieu rong la: {hinhChuNhat1.chieuRong}')
print(f"Dien tich hinh chu nhat 1 la: {hinhChuNhat1.tinhDienTich()}")

hinhVuong1 = HinhVuong(4)
hinhVuong2 = HinhVuong(5)
hinhVuong3 = HinhVuong(6)
print(f"Dien tich hinh vuong 1 la: {hinhVuong1.tinhDienTich()}")

dshh = DanhSachHinhHoc()
dshh.themHinhHoc(hinhTron1, hinhTron2, hinhTron3)
dshh.themHinhHoc(hinhChuNhat1, hinhChuNhat2, hinhChuNhat3)
dshh.themHinhHoc(hinhVuong1, hinhVuong2, hinhVuong3)
dshh.xuat()

print(f"Tong dien tich cua cac hinh la: {dshh.tinhTongDienTich()}")

print(f"Hinh tron co dien tich lon nhat la: "
      f"{dshh.timHinhCoDienTichLonNhatTheoLoaiHinh(LoaiHinh.HinhTron.value)}")
print(f"Hinh vuong co dien tich lon nhat la: "
      f"{dshh.timHinhCoDienTichLonNhatTheoLoaiHinh(LoaiHinh.HinhVuong.value)}")
print(f"Hinh chu nhat co dien tich lon nhat la: "
      f"{dshh.timHinhCoDienTichLonNhatTheoLoaiHinh(LoaiHinh.HinhChuNhat.value)}")
print(f"Hinh hoc co dien tich lon nhat la: "
      f"{dshh.timHinhCoDienTichLonNhatTheoLoaiHinh(LoaiHinh.TatCa.value)}")

print(f'So luong hinh tron la: '
      f'{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.HinhTron.value)}')
print(f'So luong hinh chu nhat la: '
      f'{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.HinhChuNhat.value)}')
print(f'So luong hinh vuong la: '
      f'{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.HinhVuong.value)}')
print(f'So luong hinh hoc la: '
      f'{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.TatCa.value)}')

print('Xuat hinh theo chieu tang giam: ')
dshh.xuatHinhTheoChieuTangGiam(LoaiHinh.HinhVuong.value)

print(f'Tong dien tich hinh vuong la: '
      f'{dshh.tinhTongDTTheoKieuHinh(LoaiHinh.HinhVuong.value)}')
