import qrcode
from os import remove
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize, Slot
from PySide6.QtWidgets import  QPushButton, QFileDialog
from my_package.components.constants import (
    STYLE_QRCODE_BUTTON, STYLE_CLEAR_BUTTON, STYLE_SAVE_BUTTON,
    SIZE_QRCODE, WIDTH_BUTTON, HEIGHT_BUTTON, PNG_PATH)
from my_package.components.utils import is_empty, validated_link
from my_package.components.input_text import InputText
from my_package.components.display import Display
from my_package.components.main_window import MainWindow



class QRCodeButton(QPushButton):

    def __init__(self, input_text: InputText | None = None,
         display: Display | None = None, window: MainWindow | None = None) -> None:
        
        super().__init__()
        self._input = input_text
        self._display = display
        self._window = window

        #Chamada de métodos
        self._style()
        #Conectando Slot()
        self.clicked.connect(self._qrcode_maker)

    def _style(self) -> None:

        self.setText("Enviar")
        self.setStyleSheet(STYLE_QRCODE_BUTTON)
        self.setFixedSize(WIDTH_BUTTON,HEIGHT_BUTTON)

    # ========== Métodos Adicionais da Classe ==========

    Slot()
    def _qrcode_maker(self) -> None:

        if isinstance(self._input, InputText) and not is_empty(self._input.text()):

            if validated_link(self._input.text()):

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
                return None
            
            return self._information("URL não identificada.")

        return self._information("Adicione uma URL para gerar o QR Code.")

    def _information(self, text: str) -> None:

        if isinstance(self._window, MainWindow):

            msg = self._window.make_message_box()
            msg.setText(text) 
            msg.setStandardButtons(msg.StandardButton.Ok)
            msg.setWindowTitle("Informação") #titulo do aviso
            msg.setIcon(msg.Icon.Information)
            msg.exec() 

class ClearButton(QPushButton):

    def __init__(self, input_text: InputText | None = None,
         display: Display | None = None) -> None:
        
        super().__init__()
        self._input_text = input_text
        self._display = display
        #Chamada de métodos
        self._style()
        #Conectando Slot()
        self.clicked.connect(self._clear)

    def _style(self) -> None:
        self.setText("Limpar")
        self.setStyleSheet(STYLE_CLEAR_BUTTON)
        self.setFixedSize(WIDTH_BUTTON,HEIGHT_BUTTON)

    # ========== Métodos Adicionais da Classe ==========

    Slot()
    def _clear(self) ->None:
        if isinstance(self._input_text, InputText):
            self._input_text.clear()
        if isinstance(self._display, Display):
            self._display.clear()

class SaveButton(QPushButton):
    def __init__(self, display: Display | None = None,
        window: MainWindow | None = None) -> None:
        super().__init__()
        self._display = display
        self._window = window

        #Chamando métodos
        self._style()
        #Conectando Slot()
        self.clicked.connect(self._save_img)

    def _style(self) -> None:
        self.setText("Salvar")
        self.setStyleSheet(STYLE_SAVE_BUTTON)
        self.setFixedSize(WIDTH_BUTTON,HEIGHT_BUTTON)

    # ========== Métodos Adicionais da Classe ==========

    Slot()
    def _save_img(self) -> None:

        #Instância da classe
        file = QFileDialog()
        if isinstance(self._display, Display) and not self._display.pixmap().isNull():
                #Pega pixmap do display, ou seja, a imagem do QR Code
                img = self._display.pixmap()
                #Usa file para abrir o gerenciador de arquivo
                file_path = file.getSaveFileName()[0]
                #Adiciona o .png
                file = file_path + ".png"
                #Salva o arquivo diretamente na classe pixmap
                img.save(file, "PNG")
                if PNG_PATH.exists():
                    remove(PNG_PATH)
                return None
        return self._critical_erro("Não tem nenhum QR Code para salvar.")
    
    def _critical_erro(self, text: str) -> None:
        if isinstance(self._window, MainWindow):
            msg = self._window.make_message_box()
            msg.setText(text)
            msg.setStandardButtons(msg.StandardButton.Ok)
            msg.setWindowTitle("Informação") 
            msg.setIcon(msg.Icon.Critical)
            msg.exec() 