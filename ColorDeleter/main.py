from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont, QIcon
from config import WND_WIDTH, WND_HEIGHT, SIZE, DY, FNT_SIZE, FNT_PATH, TITLE, ICO_PATH, TITLE
from modemenu import ModeMenu
from inpmenu import InputMenu
from outmenu import OutputMenu
from colormenu import ColorMenu
from rmmenu import RmMenu
from remover import Remover
import sys
import os


class ColorKiller(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(WND_WIDTH, WND_HEIGHT)
        icon: QIcon = QIcon(ICO_PATH)
        self.setWindowIcon(icon)
        self.setWindowTitle(TITLE)
        font: QFont = QFont(FNT_PATH, FNT_SIZE)
        line_h: int = int(DY * 1.3)
        
        mm_size: tuple[int, int] = WND_WIDTH, line_h
        mm_pos: tuple[int, int] = 0, 0
        self.mode_menu: ModeMenu = ModeMenu(self, font, mm_pos, mm_size)
        
        im_size: tuple[int, int] = WND_WIDTH, line_h * 3
        im_pos: tuple[int, int] = 0, mm_size[1]
        self.input_menu: InputMenu = InputMenu(self, font, im_pos, im_size)
        
        oi_size: tuple[int, int] = im_size
        oi_pos: tuple[int, int] = 0, im_pos[1] + im_size[1]
        self.output_menu: OutputMenu = OutputMenu(self, font, oi_pos, oi_size)
        
        cm_size: tuple[int, int] = WND_WIDTH, line_h * 4
        cm_pos: tuple[int, int] = 0, oi_pos[1] + oi_size[1]
        self.color_menu: ColorMenu = ColorMenu(self, font, cm_pos, cm_size)
        
        rm_size: tuple[int, int] = WND_WIDTH, WND_HEIGHT - mm_size[1] - im_size[1] - oi_size[1] - cm_size[1]
        rm_pos: tuple[int, int] = 0, cm_pos[1] + cm_size[1]
        self.rm_menu: RmMenu = RmMenu(self, font, rm_pos, rm_size)
        
        self.change_inp_out()
        
        self.connect_btns()
    
    def connect_btns(self) -> None:
        self.mode_menu.btn_conf.clicked.connect(self.change_inp_out)
        self.rm_menu.btn.clicked.connect(self.remove_color)
        self.rm_menu.btn_quit.clicked.connect(QApplication.quit)
    
    def remove_color(self) -> None:
        if (self.input_menu.dir == '') or (self.input_menu.filemode and (self.input_menu.filename == '')):
            return
        inp_path: str = f'{self.input_menu.dir}/{self.input_menu.filename}'
        if not os.path.exists(inp_path):
            return
        if self.output_menu.dir == '':
            self.output_menu.dir = self.input_menu.dir
        if self.output_menu.filemode:
            self.res_filename()
        if not os.path.exists(self.output_menu.dir):
            os.mkdir(self.output_menu.dir)
        out_path: str = f'{self.output_menu.dir}/{self.output_menu.filename}'
        rm_src: bool = self.rm_menu.remove_source()
        Remover.remove_color(inp_path, out_path, self.input_menu.filemode, self.color_menu.color, rm_src)
    
    def res_filename(self) -> None:
        if self.output_menu.filename == '':
            fullname: list[str] = self.input_menu.filename.split('.')
            self.output_menu.filename = f'{fullname[0]}.png'
        if not self.output_menu.filename.endswith('.png'):
            fullname: list[str] = self.output_menu.filename.split('.')
            self.output_menu.filename = f'{fullname[0]}.png'
    
    def change_inp_out(self):
        checkeds: list[bool] = [radio.isChecked() for radio in self.mode_menu.radios]
        ch_ind: int = checkeds.index(True)
        if ch_ind == 0:
            self.input_menu.filemode = True
        else:
            self.input_menu.filemode = False
        self.output_menu.filemode = self.input_menu.filemode
        self.input_menu.change_mode()
        self.output_menu.change_mode()


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    turtle: ColorKiller = ColorKiller()
    turtle.show()
    sys.exit(app.exec_())
    