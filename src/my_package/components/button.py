import qrcode
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize, Slot
from PySide6.QtWidgets import  QPushButton, QDialogButtonBox
from my_package.components.constants import (
    STYLE_QRCODE_BUTTON, STYLE_CLEAR_BUTTON, 
    SIZE_QRCODE, WIDTH_BUTTON, HEIGHT_BUTTON)
from my_package.components.input_text import InputText
from my_package.components.display import Display



class QRCodeButton(QPushButton):

    def __init__(self, input_text: InputText | None = None,
         display: Display | None = None) -> None:
        super().__init__()
        self._input = input_text
        self._display = display

        #Chamada de métodos
        self._style()
        #Conectando Slot()
        self.clicked.connect(self._qrcode_maker)

    def _style(self) -> None:

        self.setText("Enviar")
        self.setStyleSheet(STYLE_QRCODE_BUTTON)
        self.setFixedSize(WIDTH_BUTTON,HEIGHT_BUTTON)
    Slot()
    def _qrcode_maker(self) -> None:

        if isinstance(self._input, InputText):
            target_size = QSize(SIZE_QRCODE,SIZE_QRCODE)
            #Captura o texto dentro do input_text
            text = self._input.text()
            #Gera o qr code
            generic_qrcode = qrcode.make(text)
            #Convert pil.PilImage em image.image
            img = generic_qrcode.get_image()
            #Converte o qr code em QImage
            qimage = ImageQt(img)
            #Retorna o QImage como QPixmap
            image = QPixmap.fromImage(qimage)
            #Redimensinando a imagem matendo o tamanho igual
            image = image.scaled(target_size, Qt.AspectRatioMode.KeepAspectRatio)
            #Envia o QPixmap para o display(Qlabel)
            if isinstance(self._display, Display):
                self._display.add_image(image)

class ClearButton(QPushButton):
    def __init__(self, input_text: InputText | None = None,
         display: Display | None = None) -> None:
        super().__init__()
        self._input_text = input_text
        self._display = display
        #Chamada de métodos
        self._style()
        #Conectando Slo()
        self.clicked.connect(self._clear)
    def _style(self) -> None:
        self.setText("Limpar")
        self.setStyleSheet(STYLE_CLEAR_BUTTON)
        self.setFixedSize(WIDTH_BUTTON,HEIGHT_BUTTON)
    Slot()
    def _clear(self) ->None:
        if isinstance(self._input_text, InputText):
            self._input_text.clear()
        if isinstance(self._display, Display):
            self._display.clear()

class SaveButton(QDialogButtonBox):
    pass