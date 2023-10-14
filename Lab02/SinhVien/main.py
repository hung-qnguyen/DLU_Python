from ds_sinh_vien import DanhSachSv
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiChinhQuy


sv1 = SinhVienChinhQuy(1957690, "Trần Văn A", "23/6/1999", 80)
sv2 = SinhVienChinhQuy(1957691, "Nguyễn Văn C", "5/12/1999", 90)
sv3 = SinhVienPhiChinhQuy(1957692, "Thái Thị Thu", "15/8/1998", "Cao đẳng", 2)
sv4 = SinhVienPhiChinhQuy(2000324, "Trần Thanh Tâm", "27/8/2000",
                          "Cao đẳng", 2)
sv5 = SinhVienPhiChinhQuy(2004544, " Nguyễn Thanh Trà ", "15/8/1999",
                          "Trung cấp", 2.5)
sv6 = SinhVienChinhQuy(2004567, "Nguyễn Thành Nam", "7/12/1999", 69)
sv7 = SinhVienPhiChinhQuy(2004545, "Nguyễn Thanh Thanh", "29/10/1999",
                          "Trung cấp", 2.5)
sv8 = SinhVienChinhQuy(2004679, "Võ Hoài Nam", "4/1/2000", 70)

dssv = DanhSachSv()
dssv.themSinhVien(sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8)
dssv.xuat()