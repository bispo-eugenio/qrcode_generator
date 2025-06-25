from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from my_package.components.constants import STYLE_DISPLAY, SIZE_QRCODE

class Display(QLabel):

    def __init__(self ) -> None:
        super().__init__() 
        self._style()
    
    def _style(self) -> None:
        
        self.setStyleSheet(STYLE_DISPLAY)
        self.setFixedSize(SIZE_QRCODE, SIZE_QRCODE)

    # ========== Métodos Adicionais da Classe ==========
    
    def add_image(self, qrcode_img: QPixmap) -> None:
        if not qrcode_img.isNull():

            self.setPixmap(qrcode_img)
            self.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.update()