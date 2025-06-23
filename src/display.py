from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtGui import QPixmap
from my_package.constants import SIZE_QRCODE, STYLE_DISPLAY

class Display(QLabel):

    def __init__(self,
    parent: QWidget | None = None, *args, **kwargs) -> None: #type: ignore
        super().__init__(parent, *args, **kwargs) #type: ignore
        self._display_config()
        self._style()

    def _display_config(self) -> None:
        self.setFixedSize(SIZE_QRCODE, SIZE_QRCODE)
    
    def _style(self) -> None:
        self.setStyleSheet(STYLE_DISPLAY)

    def add_image(self, qrcode_img: QPixmap) -> None:
        self.setPixmap(qrcode_img)