import enum

from hinh_hoc import HinhHoc
from hinh_chu_nhat import HinhChuNhat
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong


class LoaiHinh(enum.Enum):
    TatCa = HinhHoc
    HinhTron = HinhTron
    HinhVuong = HinhVuong
    HinhChuNhat = HinhChuNhat
