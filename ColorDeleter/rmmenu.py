from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QRadioButton, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from config import SIZE, DY, BORDER


class RmMenu(QWidget):
    def __init__(self,
                 master: QMainWindow,
                 font: QFont,
                 pos: tuple[int, int],
                 size: tuple[int, int]) -> None:
        super().__init__(master)
        self.setFixedSize(size[0], size[1])
        self.move(pos[0], pos[1])
        self.layt: QGridLayout = QGridLayout(self)
        
        lbl_txt: str = 'Remove source files'
        lbl_size: tuple[int, int] = SIZE * 8, DY
        self.lbl1: QLabel = QLabel(self)
        self.lbl1.setText(lbl_txt)
        self.lbl1.setFont(font)
        self.lbl1.setStyleSheet(BORDER)
        self.lbl1.setFixedSize(lbl_size[0], lbl_size[1])
        self.layt.addWidget(self.lbl1, 0, 0)
        
        rad_txt: tuple[str, ...] = 'Yes', 'No'
        rad_size: tuple[int, int] = SIZE * 3, DY
        self.radios: list[QRadioButton] = [QRadioButton(self) for _ in range(len(rad_txt))]
        self.radios[0].setChecked(True)
        for i, radio in enumerate(self.radios, start=1):
            radio.setText(rad_txt[i - 1])
            radio.setFixedSize(rad_size[0], rad_size[1])
            radio.setFont(font)
            self.layt.addWidget(radio, 0, i)
        
        btn_txt: str = 'Start'
        btn_size: tuple[int, int] = SIZE * 5, DY
        self.btn: QPushButton = QPushButton(self)
        self.make_btn(font, self.btn, btn_txt, btn_size)
        self.layt.addWidget(self.btn, 1, 0)
        
        btnq_txt: str = 'Quit'
        btnq_size: tuple[int, int] = SIZE * 3, DY
        self.btn_quit: QPushButton = QPushButton(self)
        self.make_btn(font, self.btn_quit, btnq_txt, btnq_size)
        self.layt.addWidget(self.btn_quit, 1, len(self.radios) + 1)
    
    def remove_source(self) -> bool:
        checked: list[bool] = [radio.isChecked() for radio in self.radios]
        ind: int = checked.index(True)
        return ind == 0
    
    def make_btn(self,
                 font: QFont,
                 btn: QPushButton,
                 txt: str,
                 size: tuple[int, int]) -> None:
        btn.setText(txt)
        btn.setFont(font)
        btn.setFixedSize(size[0], size[1])
