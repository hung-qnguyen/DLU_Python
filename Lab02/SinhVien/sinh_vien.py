import datetime

class SinhVien:
    truong = "Dai hoc Da Lat"

    def __init__(self, *args) -> None:
        if len(args) == 3:
            self.__maSo: int = args[0]
            self.__hoTen: str = args[1]
            self.__ngaySinh: datetime = self.dateParse(args[2])
        elif len(args) == 1:
            dong = args[0].strip().split('%')
            self.__maSo: int = dong[0]
            self.__hoTen: str = dong[1]
            self.__ngaySinh: datetime = self.dateParse(dong[2])

    @staticmethod
    def dateParse(date: str):
        return datetime.datetime.strptime(date, "%d/%m/%Y")

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, ma_so: int):
        if self.maSoHopLe(ma_so):
            self.__maSo = ma_so

    @property
    def hoTen(self):
        return self.__hoTen

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @staticmethod
    def maSoHopLe(ma_so: int):
        return len(str(ma_so)) == 7

    @classmethod
    def doiTenTruong(cls, ten_truong: str):
        cls.truong = ten_truong

    def __str__(self):
        return f'{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}'

    def Xuat(self):
        print(f'{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}')