import sys
from my_package.components.main_window import MainWindow
from PySide6.QtWidgets import QApplication
def main() -> None:
    #Instância das classes
    app = QApplication(sys.argv)
    main_window = MainWindow()

    #Execução do programa
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()
