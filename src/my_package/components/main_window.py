from PySide6.QtWidgets import (QMainWindow, QWidget, 
                               QHBoxLayout, QLayout)
from my_package.constants import WIDTH, HEIGTH, STYLE_MAIN_WINDOW



class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None: #type: ignore
        super().__init__(*args, **kwargs) #type: ignore

        #Propriedades
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self._layout_h_box = QHBoxLayout()
        self.central.setLayout(self._layout_h_box)

        #Chamada de métodos 
        self._config_main_window()
        self._style()

    #Configura o MainWindow
    def _config_main_window(self) -> None:
        self.setWindowTitle("QRCODE GENERATOR")
        self.adjustSize() #Ajustando o tamanho dos widgets
        self.setFixedSize(WIDTH, HEIGTH)
    
    # ========== Métodos Adicionais da Classe ==========
    
    def _style(self) -> None:
        self.setStyleSheet(STYLE_MAIN_WINDOW)

    def add_layout(self, layout: QLayout) -> None:
        self._layout_h_box.addLayout(layout)

    def add_widget(self, widget: QWidget) -> None:
        self._layout_h_box.addWidget(widget)