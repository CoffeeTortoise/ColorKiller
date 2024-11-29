from PyQt5.QtWidgets import QMainWindow, QWidget, QSlider, QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from config import SIZE, BORDER, DY
from rectshape import RectangleShape


class ColorMenu(QWidget):
    def __init__(self,
                 master: QMainWindow,
                 font: QFont,
                 pos: tuple[int, int],
                 size: tuple[int, int]) -> None:
        super().__init__(master)
        self.setFixedSize(size[0], size[1])
        self.move(pos[0], pos[1])
        self.layout: QGridLayout = QGridLayout(self)
        
        lbl_txt: tuple[str, ...] = 'Red', 'Green', 'Blue'
        lbl_size: tuple[int, int] = SIZE * 4, DY
        self.lbls_m: list[QLabel] = [QLabel(self) for _ in range(len(lbl_txt))]
        
        sl_size: tuple[int, int] = SIZE * 11, DY
        self.sl_m: list[QSlider] = [QSlider(self) for _ in range(len(self.lbls_m))]
        
        lbl_nsize: tuple[int, int] = SIZE * 4, DY
        self.lbls_n: list[QLabel] = [QLabel(self) for _ in range(len(self.lbls_m))]
        for i, lbl in enumerate(self.lbls_m):
            lbl.setFont(font)
            lbl.setText(lbl_txt[i])
            lbl.setFixedSize(lbl_size[0], lbl_size[1])
            lbl.setStyleSheet(BORDER)
            self.layout.addWidget(lbl, i, 0)
            
            self.sl_m[i].setMinimum(0)
            self.sl_m[i].setMaximum(255)
            self.sl_m[i].setOrientation(1)
            self.sl_m[i].setFixedSize(sl_size[0], sl_size[1])
            self.sl_m[i].setFont(font)
            self.sl_m[i].valueChanged.connect(self.show_values)
            self.layout.addWidget(self.sl_m[i], i, 1)
            
            self.lbls_n[i].setText('0')
            self.lbls_n[i].setFont(font)
            self.lbls_n[i].setStyleSheet(BORDER)
            self.lbls_n[i].setFixedSize(lbl_nsize[0], lbl_nsize[1])
            self.layout.addWidget(self.lbls_n[i], i, 2)
        
        self.color: tuple[int, int, int] = 0, 0, 0
        self.cv_size: tuple[int, int] = sl_size[0], SIZE * 2
        self.init_canvas()
        
        btn_txt: tuple[str, ...] = 'Check', 'Confirm'
        btn_size: tuple[int, int] = SIZE * 4, SIZE * 2
        self.btns: list[QPushButton] = [QPushButton(txt, self) for txt in btn_txt]
        for btn in self.btns:
            btn.setFont(font)
            btn.setFixedSize(btn_size[0], btn_size[1])
        self.btns[0].clicked.connect(self.check_color)
        self.btns[1].clicked.connect(self.confirm_color)
        self.layout.addWidget(self.btns[0], len(self.lbls_m), 0)
        self.layout.addWidget(self.btns[1], len(self.lbls_m), 2)
    
    def show_values(self) -> None:
        for i, slide in enumerate(self.sl_m):
            val: int = slide.value()
            self.lbls_n[i].setText(str(val))
    
    def check_color(self) -> None:
        self.confirm_color()
        self.init_canvas()
    
    def confirm_color(self) -> None:
        color: tuple[int, ...] = tuple([slide.value() for slide in self.sl_m])
        if color != self.color:
            self.color = color
    
    def init_canvas(self) -> None:
        canvas: RectangleShape = RectangleShape(self, self.cv_size, self.color)
        self.layout.addWidget(canvas, len(self.lbls_m), 1)
