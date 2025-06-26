from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from my_package.components.constants import STYLE_INPUT_TEXT, MARGIN_INPUT_TEXT


class InputText(QLineEdit):
    
    def __init__(self) -> None:
        super().__init__()
        self._style()

    def _style(self) -> None:

        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setTextMargins(*[MARGIN_INPUT_TEXT for _ in range(4)])
        self.setStyleSheet(STYLE_INPUT_TEXT)
        self.setFixedSize(300, 40)