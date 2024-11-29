from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QFont
from inpmenu import InputMenu


class OutputMenu(InputMenu):
    def __init__(self,
                 master: QMainWindow,
                 font: QFont,
                 pos: tuple[int, int],
                 size: tuple[int, int]) -> None:
        super().__init__(master, font, pos, size)
        self.in_mode = False
        lbl_txt: tuple[str, ...] = 'Directory', 'Filename', 'Output'
        for i, lbl in enumerate(self.lbls):
            lbl.setText(lbl_txt[i])
        