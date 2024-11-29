from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QRadioButton, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont
from config import SIZE, DY, BORDER


class ModeMenu(QWidget):
    def __init__(self,
                 master: QMainWindow,
                 font: QFont,
                 pos: tuple[int, int],
                 size: tuple[int, int]) -> None:
        super().__init__(master)
        self.setFixedSize(size[0], size[1])
        self.move(pos[0], pos[1])
        self.layout: QHBoxLayout = QHBoxLayout(self)
        
        lbl_txt: str = 'Mode'
        lbl_size: tuple[int, int] = SIZE * 3, DY
        self.lbl_mode: QLabel = QLabel(self)
        self.lbl_mode.setText(lbl_txt)
        self.lbl_mode.setFont(font)
        self.lbl_mode.setStyleSheet(BORDER)
        self.lbl_mode.setFixedSize(lbl_size[0], lbl_size[1])
        self.layout.addWidget(self.lbl_mode)
        
        radio_opts: tuple[str, ...] = 'File', 'Folder'
        radio_sizes: tuple[int, int] = SIZE * 4, DY
        self.radios: list[QRadioButton] = [QRadioButton(radio_opts[i], self) for i in range(len(radio_opts))]
        self.radios[0].setChecked(True)
        for radio in self.radios:
            radio.setFont(font)
            radio.setFixedSize(radio_sizes[0], radio_sizes[1])
            self.layout.addWidget(radio)
        
        btn_txt: str = 'Confirm'
        btn_sizes: tuple[int, int] = SIZE * 5, DY
        self.btn_conf: QPushButton = QPushButton(btn_txt, self)
        self.btn_conf.setFont(font)
        self.btn_conf.setFixedSize(btn_sizes[0], btn_sizes[1])
        self.layout.addWidget(self.btn_conf)
