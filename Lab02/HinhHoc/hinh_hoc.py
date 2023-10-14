from abc import abstractmethod, ABC


class HinhHoc(ABC):
    def __init__(self, cd):
        self._canh = cd

    @abstractmethod
    def tinhDienTich(self) -> float:
        pass

    @abstractmethod
    def xuat(self) -> None:
        pass
