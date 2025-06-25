from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLayout
from PySide6.QtCore import Qt
from my_package.components.button import QRCodeButton, ClearButton, SaveButton
from my_package.components.display import Display
from my_package.components.input_text import InputText

class MainLayout(QVBoxLayout):

    def __init__(self) -> None: #type: ignore
        super().__init__() #type: ignore
        self._display = Display()
        self._input_text = InputText()
        self._qrcode_button = QRCodeButton(self._input_text, self._display)
        self._clear_button = ClearButton(self._input_text, self._display)
        self._save_button = SaveButton(self._display)
        self._layout_button = QHBoxLayout()

        self._add_widget(self._display)
        self._add_widget(self._input_text) #type: ignore
        self._add_layout(self._layout_button)
        self._add_widget_layout_button(self._save_button)
        self._add_widget_layout_button(self._qrcode_button)
        self._add_widget_layout_button(self._clear_button)
        self.config_layout()

    # ========== Métodos Adicionais da Classe ==========

    def config_layout(self) -> None:
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    def _add_widget(self, widget: QWidget) -> None:
        self.addWidget(widget)

    def _add_layout(self, layout: QLayout) -> None:
        self.addLayout(layout)

    def _add_widget_layout_button(self, widget: QWidget) -> None:
        self._layout_button.addWidget(widget)
        