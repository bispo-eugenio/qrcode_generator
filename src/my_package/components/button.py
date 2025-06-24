import qrcode
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import  QPushButton
from my_package.components.constants import STYLE_QRCODE_BUTTON, SIZE_QRCODE
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
        self.clicked.connect(self.qrcode_maker)

    def _style(self) -> None:

        self.setText("Enviar")
        self.setStyleSheet(STYLE_QRCODE_BUTTON)
        self.setFixedSize(100,25)

    def qrcode_maker(self) -> None:

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
            #Redimensinando imagem matendo o Size igual
            image = image.scaled(target_size, Qt.AspectRatioMode.KeepAspectRatio)
            #Envia o QPixmap para o display(Qlabel)
            if isinstance(self._display, Display):
                self._display.add_image(image)
