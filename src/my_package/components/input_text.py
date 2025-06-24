from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from my_package.components.constants import STYLE_INPUT_TEXT, MARGIN


class InputText(QLineEdit):
    def __init__(self, *args, **kwargs) -> None: #type: ignore
        super().__init__(*args, **kwargs) #type: ignore
        self._style()

    def _style(self) -> None:
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setTextMargins(*[MARGIN for _ in range(4)])
        self.setStyleSheet(STYLE_INPUT_TEXT)
        self.setFixedSize(300, 40)