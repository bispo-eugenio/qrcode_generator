from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from my_package.components.constants import STYLE_DISPLAY, SIZE_QRCODE

class Display(QLabel):

    def __init__(self ) -> None: #type: ignore
        super().__init__() #type: ignore
        self._display_config()
        self._style()

    def _display_config(self) -> None:
        self.setFixedSize(SIZE_QRCODE, SIZE_QRCODE)
    
    def _style(self) -> None:
        self.setStyleSheet(STYLE_DISPLAY)

    def add_image(self, qrcode_img: QPixmap) -> None:
        if not qrcode_img.isNull():
            self.setPixmap(qrcode_img)
            self.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.update()
            self.adjustSize()