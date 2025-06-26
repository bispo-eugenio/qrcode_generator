from PySide6.QtWidgets import (QMainWindow, QWidget,
                            QHBoxLayout, QLayout, QMessageBox)
from PySide6.QtGui import QIcon
from my_package.components.constants import WIDTH, HEIGTH, ICON_PATH

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs) -> None: #type: ignore
        super().__init__(*args, **kwargs) #type: ignore

        #Propriedades
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self._layout_h_box = QHBoxLayout()
        self.central.setLayout(self._layout_h_box)

        #Chamada de métodos 
        self._config_main_window()

    #Configura o MainWindow
    def _config_main_window(self) -> None:

        self.setWindowIcon(QIcon(str(ICON_PATH)))
        self.setWindowTitle("QRCODE GENERATOR")
        self.adjustSize() #Ajustando o tamanho dos widgets
        self.setFixedSize(WIDTH, HEIGTH)
        self._layout_h_box.setSpacing(20)
    
    # ========== Métodos Adicionais da Classe ==========

    def add_layout(self, layout: QLayout) -> None:

        self._layout_h_box.addLayout(layout)

    def make_message_box(self) -> QMessageBox:

        return QMessageBox(self)