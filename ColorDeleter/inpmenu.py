from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from config import SIZE, DY, BORDER, NO_SYMB


class InputMenu(QWidget):
    def __init__(self,
                 master: QMainWindow,
                 font: QFont,
                 pos: tuple[int, int],
                 size: tuple[int, int]) -> None:
        super().__init__(master)
        self.setFixedSize(size[0], size[1])
        self.move(pos[0], pos[1])
        self.filemode: bool = True
        self.in_mode: bool = True
        self.layout: QGridLayout = QGridLayout(self)
        self.dir: str = ''
        self.filename: str = ''
        
        lbl_txt: tuple[str, ...] = 'Directory', 'Filename', 'Input'
        lbl_size: tuple[int, int] = SIZE * 4, DY
        self.lbls: list[QLabel]= [QLabel(self) for _ in range(len(lbl_txt))]
        for i, lbl in enumerate(self.lbls):
            lbl.setText(lbl_txt[i])
            lbl.setFont(font)
            lbl.setStyleSheet(BORDER)
            lbl.setFixedSize(lbl_size[0], lbl_size[1])
            self.layout.addWidget(lbl, i, 0)
        
        inp_size: tuple[int, int] = size[0] - lbl_size[0] - SIZE, DY
        self.inps: list[QLineEdit] = [QLineEdit(self) for _ in range(len(lbl_txt) - 1)]
        for i, line in enumerate(self.inps):
            line.setFont(font)
            line.setFixedSize(inp_size[0], inp_size[1])
            self.layout.addWidget(line, i, 1)
        
        btn_txt: str = 'Confirm'
        btn_size: tuple[int, int] = size[0] - lbl_size[0] - SIZE, DY
        self.btn_conf: QPushButton = QPushButton(btn_txt, self)
        self.btn_conf.setFont(font)
        self.btn_conf.setFixedSize(btn_size[0], btn_size[1])
        self.btn_conf.clicked.connect(self.get_source)
        self.layout.addWidget(self.btn_conf, len(self.inps), 1)
    
    def change_mode(self) -> None:
        if self.filemode:
            self.lbls[1].show()
            self.inps[1].show()
        else:
            self.lbls[1].hide()
            self.inps[1].hide()
    
    def get_source(self) -> None:
        self.dir = ''
        self.filename = ''
        dr_path: str = self.proc_path()
        name: str = self.proc_name()
        if ((dr_path == '') or (self.filemode and (name == ''))) and self.in_mode:
            return
        self.dir = dr_path
        if self.filemode:
            self.filename = name
    
    def proc_path(self) -> str:
        path: str = self.inps[0].text()
        dr: str = ''.join(['' if (sym in NO_SYMB) else sym for sym in path]).replace('\\', '/')
        if dr.endswith('/'):
            old: str = dr
            dr = old[:len(old) - 1]
        return dr
    
    def proc_name(self) -> str:
        if self.filemode:
            name: str = self.inps[1].text()
            nm: str = ''.join(['' if (sym in NO_SYMB) else sym for sym in name]).replace('\\', '/').replace('/', '')
            return nm
        else:
            return ''
