from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPainter


class RectangleShape(QWidget):
    def __init__(self,
                 master: QWidget,
                 size: tuple[int, int],
                 color: tuple[int, int, int]) -> None:
        super().__init__(master)
        self.setFixedSize(size[0], size[1])
        self.color: tuple[int, int, int] = color
        self.pos: tuple[int, int] = 0, 0
    
    def move(self, x: int,
             y: int) -> None:
        super().move(x, y)
        self.pos = x, y
    
    def paintEvent(self, event) -> None:
        painter: QPainter = QPainter(self)
        painter.setBrush(QColor(self.color[0], self.color[1], self.color[2]))
        painter.drawRect(self.pos[0], self.pos[1], self.width(), self.height())
